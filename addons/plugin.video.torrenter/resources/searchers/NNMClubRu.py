#-*- coding: utf-8 -*-
'''
    Torrenter plugin for XBMC
    Copyright (C) 2011 Vadim Skorba
    vadim.skorba@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

searchRequestUrl = "http://playble.ru/data/4.php?q=%s&section=video"
searchRegularExpression = "data-title=\"(.+?)\".+?<td><a href=\"(.+?)\".+?<td>\s?(\d+)</td>"
searchIcon = '/resources/searchers/icons/nnm-club.ru.png'
isMagnetLinkSource = False
sourceWeight = 1
