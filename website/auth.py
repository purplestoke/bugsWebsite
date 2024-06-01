from flask import Flask, render_template, request, Blueprint, redirect
import requests

auth = Blueprint("auth", __name__)
