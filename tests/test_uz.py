# -*- coding: utf-8 -*-
# Авторские права (c) 2003, Taro Ogawa.  Все права защищены.
# Авторские права (c) 2013, Savoir-faire Linux inc.  Все права защищены.

# Эта библиотека является свободным программным обеспечением; вы можете его распространять и (или)
# изменять его в соответствии с Условиями GNU Lesser General Public
# Лицензия, опубликованная Free Software Foundation; либо
# версии 2.1 Лицензии, либо (по вашему выбору) любой более поздней версии.
# Эта библиотека распространяется в надежде на то, что она будет полезна,
# НО БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ; даже без подразумеваемой гарантии
# ПРИГОДНОСТЬ ДЛЯ ОПРЕДЕЛЕННЫХ ЦЕЛЕЙ. См. GNU
# Lesser General Public License для получения более подробной информации.
# Вы должны были получить копию GNU Lesser General Public
# License вместе с этой библиотекой; если нет, напишите в Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words


class Num2WordsUZTest(TestCase):
    def test_to_cardinal(self):
        self.maxDiff = None
        self.assertEqual(num2words(1, lang="uz"), "bir")
        self.assertEqual(num2words(23, lang="uz"), "yigirma uch")
        self.assertEqual(num2words(145, lang="uz"), "yuz qirq besh")
        self.assertEqual(
            num2words(2869, lang="uz"),
            "ikki ming sakkiz yuz oltmish to\'qqiz"
        )
        self.assertEqual(
            num2words(-789000125, lang="uz"),
            "minus etti yuz sakson to\'qqiz million yuz yigirma besh",
        )
        self.assertEqual(
            num2words(84932, lang="uz"), "sakson tort ming to'qqiz yuz o'ttiz ikki"
        )

    def test_to_cardinal_floats(self):
        self.assertEqual(num2words(100.67, lang="uz"), "yuz butun oltmish etti")
        self.assertEqual(num2words(0.7, lang="uz"), "nol butun etti")
        self.assertEqual(num2words(1.73, lang="uz"), "bir butun etmish uch")
        self.assertEqual(
            num2words(10.02, lang='uz'),
            "on butun nol ikki"
        )
        self.assertEqual(
            num2words(15.007, lang='uz'),
            "on besh butun nol nol etti"
        )

    def test_to_ordinal(self):
        with self.assertRaises(NotImplementedError):
            num2words(1, lang="uz", to="ordinal")

    def test_to_currency(self):
        self.assertEqual(
            num2words(25.24, lang="uz", to="currency", currency="UZS"),
            "yigirma besh so'm, yigirma tort tiyin",
        )
        self.assertEqual(
            num2words(1996.4, lang="uz", to="currency", currency="UZS"),
            "bir ming to'qqiz yuz to'qson olti so'm, qirq tiyin",
        )
        self.assertEqual(
            num2words(632924.51, lang="uz", to="currency", currency="UZS"),
            "olti yuz o'ttiz ikki ming to'qqiz yuz yigirma tort so'm, ellik bir tiyin",
        )
