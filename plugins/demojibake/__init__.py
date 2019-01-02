# -*- coding: utf-8 -*-

# demojibake: Repairs tag metadata encoding.
# Copyright (C) 2019  Edontin
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

PLUGIN_NAME = 'DeMojibake'
PLUGIN_AUTHOR = 'Edontin'
PLUGIN_DESCRIPTION = """This plugin allows incorrectly-encoded tags to be repaired.
Supports repairing file groups e.g. clusters."""
PLUGIN_VERSION = '0.1'
PLUGIN_API_VERSIONS = ['2.0']
PLUGIN_LICENSE = 'GPL-2.0-or-later'
PLUGIN_LICENSE_URL = 'https://www.gnu.org/licenses/gpl-2.0.html'

from picard.plugins.demojibake\
        .fix_metadata_encoding_dialog import Ui_FixMetadataEncodingDialog
from picard.ui.itemviews import *
from PyQt5 import QtCore, QtWidgets
from picard import log
import itertools
import sys

try:
    from picard.util.tags import PRESERVED_TAGS
except ImportError:
    from picard.file import File
    PRESERVED_TAGS = File._default_preserved_tags


class FixMetadataEncodingAction(BaseAction):
    NAME = 'Repair metadata encoding...'

    def _try_reverse_encoding(
            self,
            value,
            dst_encoding,
            src_encodings=[sys.getdefaultencoding(), 'utf_8', 'latin_1']):
        for encoding in src_encodings:
            try:
                return value.encode(encoding).decode(dst_encoding)
            except UnicodeError as e:
                log.info('Failure to perform conversion %s -> %s: %s' %
                         (encoding, dst_encoding, e))
                pass
        return None

    def _encode_tags_in_file(self, src_file, tags, dst_encoding):
        for tag in tags:
            try:
                result = self._try_reverse_encoding(src_file.metadata[tag],
                                                    dst_encoding)
            except KeyError:
                continue
            if result:
                src_file.metadata[tag] = result
                src_file.changed = True
            else:
                log.warning('Failure performing conversion to %s for tag %s' %
                            (dst_encoding, tag))
        src_file.update(signal=True)

    def callback(self, objs):
        preserved_tags = set(PRESERVED_TAGS)
        files = [y for x in objs for y in x.iterfiles()]
        tag_keys = {
            y
            for x in files for y in x.metadata.keys()
            if not (y.startswith('~') or y in preserved_tags)
        }
        log.debug('Available tags in file(s): %s' % tag_keys)
        dialog = ViewFixEncodingDialog(tag_keys)
        if dialog.exec_() != QtWidgets.QDialog.Accepted:
            return

        selected_tags = dialog.get_selected_tags()
        dst_encoding = dialog.get_dst_encoding()
        log.debug('Fixing tag(s): %s' % selected_tags)
        try:
            for src_file in files:
                self._encode_tags_in_file(src_file, selected_tags,
                                          dst_encoding)
        except LookupError:
            log.error('Invalid encoding requested: %s' % dst_encoding)


class ViewFixEncodingDialog(QtWidgets.QDialog):
    def __init__(self, available_meta_keys, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_FixMetadataEncodingDialog()
        self.ui.setupUi(self)
        for meta_key in available_meta_keys:
            item = QtWidgets.QTreeWidgetItem()
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setText(0, meta_key)
            item.setCheckState(0, QtCore.Qt.Unchecked)
            self.ui.metadataFieldsTreeView.addTopLevelItem(item)

    def get_dst_encoding(self):
        return self.ui.appliedEncodingLineEdit.text()

    def get_selected_tags(self):
        items = []
        root_item = self.ui.metadataFieldsTreeView.invisibleRootItem()

        for i in range(root_item.childCount()):
            child_item = root_item.child(i)
            if child_item.checkState(0) == QtCore.Qt.Checked:
                items.append(child_item.text(0))
        return items


fix_enc_action = FixMetadataEncodingAction()
register_file_action(fix_enc_action)
register_track_action(fix_enc_action)
register_album_action(fix_enc_action)
register_cluster_action(fix_enc_action)
register_clusterlist_action(fix_enc_action)
