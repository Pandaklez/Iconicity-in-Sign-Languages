from app import db, app

class Base(db.Model):
    __searchable__ = ['word', 'semantic_field']
    
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(60), index=True, unique=True)
    semantic_field = db.Column(db.String(120), index=True)
    template = db.Column(db.String(120), index=True, unique=True)
    languages = db.relationship('Languages', backref='phr_html', lazy='dynamic')

    def __repr__(self):
        return '<Base %r>' % (self.word)
        
class Languages(db.Model):
    __searchable__ = ['language', 'icon_pattern', 'expression_pattern']
    
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(120), index=True)
    nonicon = db.Column(db.String(20), index=True)
    url = db.Column(db.String(120), index=True, unique=True)
    icon_pattern = db.Column(db.String(120), index=True)
    expression_pattern = db.Column(db.String(120), index=True)
    word_id = db.Column(db.Integer, db.ForeignKey('base.id'))

    def __repr__(self):
        return '<Languages %r>' % (self.language)
