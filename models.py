from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Company(db.Model):
    __tablename__='company'
    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String, unique=True, nullable=False)
    overall_aum = db.Column(db.Integer, nullable=False)

class Scheme(db.Model):
    __tablename__='scheme'
    scheme_id = db.Column(db.Integer, primary_key=True)
    inception_date = db.Column(db.DateTime, default=datetime.datetime.now)
    scheme_name = db.Column(db.String, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.company_id'), nullable=False)
    scheme_type = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)

class Performance_Parameters(db.Model):
    __tablename__='performance_parameters'
    scheme_id = db.Column(db.Integer, db.ForeignKey('scheme.scheme_id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    r_nav = db.Column(db.Float, nullable=False)
    r_returns = db.Column(db.Float, nullable=False)
    r_aum = db.Column(db.Float, nullable=False)
    d_nav = db.Column(db.Float, nullable=False)
    d_returns = db.Column(db.Float, nullable=False)
    d_aum = db.Column(db.Float, nullable=False)

class Benchmark(db.Model):
    __tablename__='benchmark'
    benchmark_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    benchmark_name = db.Column(db.String, nullable=False)
    value = db.column(db.Float, nullable=False)