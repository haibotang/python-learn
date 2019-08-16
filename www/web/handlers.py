#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from www.web.coroweb import get, post

from www.models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }

@get('/api/users')
def api_get_users():
    users = yield from User.findAll()
    for u in users:
        u.passwd = '******'
    return dict(users=users)