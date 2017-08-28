# -*- coding: utf-8 -*- 
"""
@author: xujingyi
@date: 2017/8/28
"""
# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash