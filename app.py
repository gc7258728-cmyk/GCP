# -*- coding: utf-8 -*-
# Génie Civil Pro : application autonome, données séparées du code.
SCHEMA_SQL = "CREATE TABLE IF NOT EXISTS utilisateurs (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                identifiant TEXT UNIQUE NOT NULL,\n                nom_complet TEXT NOT NULL,\n                mot_de_passe_hash TEXT NOT NULL,\n                role TEXT NOT NULL,\n                actif INTEGER NOT NULL DEFAULT 1,\n                derniere_connexion TEXT\n            );\nCREATE TABLE IF NOT EXISTS chantiers (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                code TEXT UNIQUE NOT NULL,\n                nom TEXT NOT NULL,\n                budget_fcfa REAL NOT NULL,\n                date_debut TEXT NOT NULL,\n                date_fin_prevue TEXT NOT NULL,\n                client TEXT,\n                localisation TEXT,\n                statut TEXT NOT NULL DEFAULT 'en_cours',\n                supprime INTEGER DEFAULT 0\n            );\nCREATE TABLE IF NOT EXISTS journalier (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                chantier_id INTEGER NOT NULL,\n                date_jour TEXT NOT NULL,\n                meteo TEXT,\n                effectif INTEGER,\n                travaux_realises TEXT,\n                incidents TEXT,\n                supprime INTEGER DEFAULT 0,\n                FOREIGN KEY (chantier_id) REFERENCES chantiers(id)\n            );\nCREATE TABLE IF NOT EXISTS malfacons (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                chantier_id INTEGER NOT NULL,\n                element TEXT NOT NULL,\n                type_defaut TEXT NOT NULL,\n                criticite TEXT NOT NULL,\n                description TEXT,\n                action_corrective TEXT,\n                statut_resolution TEXT NOT NULL DEFAULT 'Ouvert',\n                date_signalement TEXT NOT NULL,\n                supprime INTEGER DEFAULT 0,\n                FOREIGN KEY (chantier_id) REFERENCES chantiers(id)\n            );\nCREATE TABLE IF NOT EXISTS depenses (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                chantier_id INTEGER NOT NULL,\n                categorie TEXT NOT NULL,\n                libelle TEXT NOT NULL,\n                montant_fcfa REAL NOT NULL,\n                date_depense TEXT NOT NULL,\n                reference_piece TEXT,\n                supprime INTEGER DEFAULT 0,\n                FOREIGN KEY (chantier_id) REFERENCES chantiers(id)\n            );\nCREATE TABLE IF NOT EXISTS avancement (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                chantier_id INTEGER NOT NULL,\n                pourcentage REAL NOT NULL,\n                description TEXT,\n                date_saisie TEXT NOT NULL,\n                supprime INTEGER DEFAULT 0,\n                FOREIGN KEY (chantier_id) REFERENCES chantiers(id)\n            );\nCREATE TABLE IF NOT EXISTS materiel (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                chantier_id INTEGER NOT NULL,\n                designation TEXT NOT NULL,\n                quantite REAL NOT NULL,\n                unite TEXT NOT NULL,\n                date_reception TEXT NOT NULL,\n                supprime INTEGER DEFAULT 0,\n                FOREIGN KEY (chantier_id) REFERENCES chantiers(id)\n            );\nCREATE TABLE IF NOT EXISTS devis (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                chantier_id INTEGER NOT NULL,\n                numero TEXT UNIQUE NOT NULL,\n                objet TEXT NOT NULL,\n                tva_pct REAL NOT NULL DEFAULT 19.25,\n                statut TEXT NOT NULL DEFAULT 'brouillon',\n                supprime INTEGER DEFAULT 0,\n                FOREIGN KEY(chantier_id) REFERENCES chantiers(id)\n            );\nCREATE TABLE IF NOT EXISTS lignes_devis (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                devis_id INTEGER NOT NULL,\n                designation TEXT NOT NULL,\n                unite TEXT NOT NULL,\n                quantite REAL NOT NULL,\n                prix_unitaire_fcfa REAL NOT NULL,\n                supprime INTEGER DEFAULT 0,\n                FOREIGN KEY(devis_id) REFERENCES devis(id)\n            );\nCREATE TABLE IF NOT EXISTS historique (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                table_nom TEXT NOT NULL,\n                row_id INTEGER NOT NULL,\n                operation TEXT NOT NULL,\n                nouvelles_valeurs TEXT,\n                utilisateur TEXT,\n                ts TEXT NOT NULL\n            );\n"
EXTENSIONS_SQL = 'CREATE TABLE IF NOT EXISTS acces_chantiers (\n chantier_id INTEGER NOT NULL REFERENCES chantiers(id),\n utilisateur_id INTEGER NOT NULL REFERENCES utilisateurs(id),\n PRIMARY KEY(chantier_id,utilisateur_id)\n);\nCREATE TABLE IF NOT EXISTS photos (\n id INTEGER PRIMARY KEY AUTOINCREMENT,\n table_nom TEXT NOT NULL,\n row_id INTEGER NOT NULL,\n chantier_id INTEGER NOT NULL REFERENCES chantiers(id),\n phase TEXT NOT NULL,\n contenu BLOB NOT NULL,\n ts TEXT NOT NULL\n);\nCREATE INDEX IF NOT EXISTS idx_photos_chantier ON photos(chantier_id);\nCREATE INDEX IF NOT EXISTS idx_historique_row ON historique(table_nom,row_id);\n'
STYLE = '<style>\n/* Keyed containers belong to this app; native Streamlit widgets remain intact. */\n[class*="st-key-mobile_"] { display: none; }\n[data-testid="stMainBlockContainer"] { max-width: 1280px; }\n[data-testid="stMarkdownContainer"] { overflow-wrap: anywhere; }\n[data-testid="stMetricValue"] { overflow-wrap: anywhere; white-space: normal; }\n[data-testid="stMetricValue"] > div { white-space: normal; font-size: 1.6rem; }\nbutton p { white-space: normal; overflow-wrap: anywhere; }\n@media (max-width: 768px) {\n  [class*="st-key-desktop_"] { display: none; }\n  [class*="st-key-mobile_"] { display: block; }\n  [data-testid="stMainBlockContainer"] {\n    padding-left: 1rem;\n    padding-right: 1rem;\n    padding-top: 4.2rem;\n  }\n  [data-testid="stMarkdownContainer"] h1 { font-size: 1.75rem; }\n  [data-testid="stMarkdownContainer"] h2 { font-size: 1.4rem; }\n  [data-testid="stMarkdownContainer"] h3 { font-size: 1.15rem; }\n  button { min-height: 44px; }\n  [data-testid="stTextInput"] input { font-size: 16px; }\n  [data-testid="stTextArea"] textarea { font-size: 16px; }\n  [data-testid="stExpander"] summary p { white-space: normal; overflow-wrap: anywhere; }\n}\n@media (max-width: 640px) {\n  [data-testid="stColumn"] { width: 100%; flex: 1 1 100%; min-width: 0; }\n}\n\n:root { color-scheme: light; }\n.stApp { background: #fbfcfd; color: #23333b; }\n[data-testid="stMainBlockContainer"] { padding-top: 4.2rem; padding-bottom: 3rem; max-width: 1380px; }\n[data-testid="stSidebar"] { background: #edf3f5; border-right: 1px solid #dce5e9; }\n[data-testid="stSidebar"] h3 { color: #126c77; }\nh1,h2,h3 { color: #23333b; letter-spacing: 0 !important; }\nh1 { font-size: 2.35rem !important; font-weight: 750 !important; }\nh2 { font-size: 1.55rem !important; }\nh3 { font-size: 1.2rem !important; }\n[data-testid="stCaptionContainer"] { color: #5c737c; }\n[data-testid="stForm"] { background: white; border: 1px solid #dce5e9; border-radius: 6px; padding: 1.25rem; }\n[data-testid="stMetric"] { border-top: 3px solid #1c8391; padding: 1rem 0; }\n[data-testid="stMetricValue"] { color: #116875; }\n[data-testid="stExpander"] { background: white; border-radius: 6px; }\nbutton { border-radius: 5px !important; }\n[data-testid="stFormSubmitButton"] button { background: #126c77; color: white; border-color: #126c77; }\n[data-testid="stFormSubmitButton"] button:hover { background: #0e555e; color: white; border-color: #0e555e; }\n[data-testid="stFormSubmitButton"] button p { color: inherit; }\n[data-testid="stDownloadButton"] button { color: #126c77; border-color: #9abfc5; }\ninput,textarea { color: #23333b; }\n@media (max-width:640px) {\n  h1 { font-size: 1.85rem !important; }\n  [data-testid="stForm"] { padding: .85rem; }\n  [data-testid="stMainBlockContainer"] { padding-left: 1rem; padding-right: 1rem; }\n}\n\n</style>\n'

import datetime as dt
import hashlib
import hmac
import os
import secrets
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_ROOT = Path(os.environ.get('GENIE_CIVIL_DATA', Path.home() / 'GenieCivilProStreamlit'))
TABLES = {'chantiers', 'journalier', 'malfacons', 'depenses', 'avancement', 'materiel', 'devis', 'lignes_devis'}


class LocalDatabase:
    def __init__(self, path=None):
        self.path = Path(path or os.environ.get('GENIE_CIVIL_DB', DATA_ROOT / 'geniecivil_pro.db'))
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path, timeout=15)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute('PRAGMA foreign_keys=ON')
        self.conn.executescript(SCHEMA_SQL)

    def rows(self, sql, args=()):
        return [dict(row) for row in self.conn.execute(sql, args)]

    def write(self, sql, args=()):
        with self.conn:
            return self.conn.execute(sql, args).lastrowid

    def register(self, login, name, password, confirmation):
        login = login.strip().lower()
        if len(login) < 3 or not name.strip():
            raise ValueError('Identifiant de 3 caractères minimum et nom requis.')
        if len(password) < 8 or password != confirmation:
            raise ValueError('Mot de passe de 8 caractères minimum ; confirmations identiques.')
        # Restrict account creation after bootstrap to authenticated administrators.
        with self.conn:
            self.conn.execute('BEGIN IMMEDIATE')
            count = self.conn.execute('SELECT COUNT(*) FROM utilisateurs').fetchone()[0]
            if count and not getattr(self, 'admin', False):
                raise ValueError('Seul un administrateur peut créer les comptes suivants.')
            salt = secrets.token_hex(16)
            digest = hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt), 600000).hex()
            self.conn.execute('INSERT INTO utilisateurs (identifiant,nom_complet,mot_de_passe_hash,role) VALUES (?,?,?,?)',
                              (login, name.strip(), f'pbkdf2$600000${salt}${digest}', 'admin' if count == 0 else 'editeur'))

    def login(self, login, password):
        rows = self.rows('SELECT * FROM utilisateurs WHERE identifiant=? AND actif=1', (login.strip().lower(),))
        if not rows:
            raise ValueError('Identifiant ou mot de passe incorrect.')
        user = rows[0]
        stored = user['mot_de_passe_hash']
        if stored.startswith('pbkdf2$'):
            _, rounds, salt, expected = stored.split('$')
            actual = hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt), int(rounds)).hex()
        else:
            expected = stored
            actual = hashlib.sha256(password.encode()).hexdigest()
        if not hmac.compare_digest(actual, expected):
            raise ValueError('Identifiant ou mot de passe incorrect.')
        self.write('UPDATE utilisateurs SET derniere_connexion=? WHERE id=?', (dt.datetime.now().isoformat(), user['id']))
        return {k: user[k] for k in ('id', 'identifiant', 'nom_complet', 'role')}

    def insert(self, table, values, user):
        if table not in TABLES or user['role'] not in ('admin', 'editeur'):
            raise ValueError('Action non autorisée.')
        columns = {r['name'] for r in self.conn.execute(f'PRAGMA table_info({table})')}
        if not set(values).issubset(columns):
            raise ValueError('Champs invalides.')
        for key, val in values.items():
            if key in ('code', 'nom', 'libelle', 'designation', 'element', 'type_defaut', 'numero', 'objet', 'unite') and not str(val).strip():
                raise ValueError('Les champs obligatoires doivent être remplis.')
            if key.startswith('date_'):
                dt.date.fromisoformat(str(val))
            if key in ('budget_fcfa', 'montant_fcfa', 'quantite', 'prix_unitaire_fcfa') and float(val) < 0:
                raise ValueError('Les montants et quantités doivent être positifs.')
        if table == 'chantiers' and values['date_fin_prevue'] < values['date_debut']:
            raise ValueError('La fin prévue doit être après le début.')
        if table == 'avancement' and not 0 <= values['pourcentage'] <= 100:
            raise ValueError('Avancement attendu entre 0 et 100 %.')
        with self.conn:
            cur = self.conn.execute(f'INSERT INTO {table} ({",".join(values)}) VALUES ({",".join("?" for _ in values)})', tuple(values.values()))
            return cur.lastrowid

    def backup(self):
        import tempfile
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'sauvegarde.db'
            dest = sqlite3.connect(path)
            try:
                self.conn.backup(dest)
            finally:
                dest.close()
            return path.read_bytes()


import datetime as dt
import io
import json
import os
from contextlib import contextmanager
from pathlib import Path




class PgConnection:
    def __init__(self,url):
        import psycopg
        from psycopg.rows import dict_row
        self.raw = psycopg.connect(url,autocommit=True,row_factory=dict_row,connect_timeout=10)
    def execute(self,sql,args=()):
        return self.raw.execute(sql.replace('?', '%s'),args)
    def close(self): self.raw.close()


class Database(LocalDatabase):
    def __init__(self,path=None,url=None):
        url = url or os.environ.get('DATABASE_URL')
        self.postgres = bool(url)
        if url:
            self.conn = PgConnection(url)
            schema = SCHEMA_SQL.replace('INTEGER PRIMARY KEY AUTOINCREMENT','INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY').replace(' REAL ', ' DOUBLE PRECISION ')
            for query in schema.split(';'):
                if query.strip(): self.conn.execute(query)
        else:
            super().__init__(path)
        sql = EXTENSIONS_SQL
        if url:
            sql=sql.replace('INTEGER PRIMARY KEY AUTOINCREMENT','INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY').replace(' BLOB ', ' BYTEA ')
        with self.transaction():
            for query in sql.split(';'):
                if query.strip(): self.conn.execute(query)

    @contextmanager
    def transaction(self):
        if self.postgres:
            with self.conn.raw.transaction():
                yield
        elif self.conn.in_transaction:
            import secrets
            name='sp_'+secrets.token_hex(8)
            self.conn.execute('SAVEPOINT '+name)
            try:
                yield
                self.conn.execute('RELEASE SAVEPOINT '+name)
            except BaseException:
                self.conn.execute('ROLLBACK TO SAVEPOINT '+name)
                self.conn.execute('RELEASE SAVEPOINT '+name)
                raise
        else:
            self.conn.execute('BEGIN IMMEDIATE')
            with self.conn:
                yield

    def write(self,sql,args=()):
        with self.transaction(): return self.conn.execute(sql,args).rowcount

    def actor(self,user,edit=False,admin=False):
        found=self.rows('SELECT id,identifiant,role FROM utilisateurs WHERE id=? AND actif=1',(user.get('id'),))
        if not found or (edit and found[0]['role'] not in ('admin','editeur')) or (admin and found[0]['role']!='admin'):
            raise ValueError('Action non autorisée.')
        return found[0]

    def access(self,cid,user,edit=False):
        actor=self.actor(user,edit=edit)
        if not self.rows('SELECT id FROM chantiers WHERE id=? AND supprime=0',(cid,)):
            raise ValueError('Chantier indisponible.')
        if actor['role']!='admin' and not self.rows('SELECT chantier_id FROM acces_chantiers WHERE chantier_id=? AND utilisateur_id=?',(cid,actor['id'])):
            raise ValueError('Accès au chantier refusé.')

    def sites(self,user,archived=False):
        actor=self.actor(user)
        if actor['role']=='admin':
            return self.rows('SELECT * FROM chantiers WHERE supprime=? ORDER BY id DESC',(int(archived),))
        return self.rows('SELECT c.* FROM chantiers c JOIN acces_chantiers a ON a.chantier_id=c.id WHERE c.supprime=0 AND a.utilisateur_id=? ORDER BY c.id DESC',(actor['id'],))

    def audit(self,table,rid,operation,values,user):
        self.conn.execute('INSERT INTO historique(table_nom,row_id,operation,nouvelles_valeurs,utilisateur,ts) VALUES(?,?,?,?,?,?)',(table,rid,operation,json.dumps(values,ensure_ascii=False,default=str),user['identifiant'],dt.datetime.now(dt.timezone.utc).isoformat()))

    def register(self,login,name,password,confirmation,user=None,role='editeur'):
        import hashlib,secrets
        if len(login.strip())<3 or not name.strip() or len(password)<8 or password!=confirmation:
            raise ValueError('Nom et identifiant requis ; mot de passe de 8 caractères et confirmation identique.')
        if role not in ('admin','editeur','lecteur'): raise ValueError('Rôle invalide.')
        with self.transaction():
            if self.postgres: self.conn.execute('LOCK TABLE utilisateurs IN EXCLUSIVE MODE')
            count=self.rows('SELECT COUNT(*) total FROM utilisateurs')[0]['total']
            if count: self.actor(user or {},admin=True)
            salt=secrets.token_hex(16)
            digest=hashlib.pbkdf2_hmac('sha256',password.encode(),bytes.fromhex(salt),600000).hex()
            self.conn.execute('INSERT INTO utilisateurs(identifiant,nom_complet,mot_de_passe_hash,role) VALUES(?,?,?,?)',(login.strip().lower(),name.strip(),f'pbkdf2$600000${salt}${digest}','admin' if not count else role))

    def scope(self,table,row):
        if table=='chantiers': return row['id']
        if table=='lignes_devis':
            quotes=self.rows('SELECT chantier_id FROM devis WHERE id=? AND supprime=0',(row['devis_id'],))
            if not quotes: raise ValueError('Devis indisponible.')
            return quotes[0]['chantier_id']
        return row['chantier_id']

    def validate(self,table,values):
        import math
        if table not in TABLES: raise ValueError('Table invalide.')
        if self.postgres:
            columns={r['column_name'] for r in self.rows('SELECT column_name FROM information_schema.columns WHERE table_name=? AND table_schema=current_schema()',(table,))}
        else:
            columns={r['name'] for r in self.rows(f'PRAGMA table_info({table})')}
        if not set(values).issubset(columns-{'id','supprime'}): raise ValueError('Champs invalides.')
        for key,val in values.items():
            if key in ('code','nom','libelle','designation','element','type_defaut','numero','objet','unite') and not str(val).strip(): raise ValueError('Champs obligatoires manquants.')
            if key.startswith('date_'): dt.date.fromisoformat(str(val))
            if key in ('budget_fcfa','montant_fcfa','quantite','prix_unitaire_fcfa','effectif','pourcentage','tva_pct') and (not math.isfinite(float(val)) or float(val)<0): raise ValueError('Valeur numérique positive attendue.')
        if table=='chantiers' and values['date_fin_prevue']<values['date_debut']: raise ValueError('La fin prévue doit suivre le début.')
        if any(k in values and not 0<=values[k]<=100 for k in ('pourcentage','tva_pct')): raise ValueError('Pourcentage attendu entre 0 et 100 %.')
        enums={'statut_resolution':{'Ouvert','En cours','Résolu'},'criticite':{'Faible','Moyenne','Élevée','Critique'},'categorie':{'materiaux','main_oeuvre','materiel','sous_traitance','transport','autre'}}
        for key,allowed in enums.items():
            if key in values and values[key] not in allowed: raise ValueError('Option invalide : '+key)

    def insert(self,table,values,user):
        actor=self.actor(user,edit=True)
        self.validate(table,values)
        if table!='chantiers': self.access(self.scope(table,values),user,edit=True)
        with self.transaction():
            sql=f'INSERT INTO {table} ({",".join(values)}) VALUES ({",".join("?" for _ in values)})'
            cur=self.conn.execute(sql+(' RETURNING id' if self.postgres else ''),tuple(values.values()))
            rid=cur.fetchone()['id'] if self.postgres else cur.lastrowid
            if table=='chantiers': self.conn.execute('INSERT INTO acces_chantiers(chantier_id,utilisateur_id) VALUES(?,?)',(rid,actor['id']))
            self.audit(table,rid,'creation',values,actor)
            return rid

    def update(self,table,rid,values,user):
        actor=self.actor(user,edit=True)
        if table not in TABLES: raise ValueError('Table invalide.')
        old=self.rows(f'SELECT * FROM {table} WHERE id=? AND supprime=0',(rid,))
        if not old: raise ValueError('Enregistrement indisponible.')
        self.access(self.scope(table,old[0]),user,edit=True)
        if set(values)&{'id','supprime','chantier_id','devis_id'}: raise ValueError('Références non modifiables.')
        merged={k:v for k,v in old[0].items() if k not in ('id','supprime')}
        merged.update(values)
        self.validate(table,merged)
        with self.transaction():
            self.conn.execute(f'UPDATE {table} SET {",".join(k+"=?" for k in values)} WHERE id=?',(*values.values(),rid))
            self.audit(table,rid,'modification',{'avant':old[0],'apres':merged},actor)

    def archive(self,table,rid,user,restore=False):
        actor=self.actor(user,edit=True,admin=restore)
        if table not in TABLES: raise ValueError('Table invalide.')
        old=self.rows(f'SELECT * FROM {table} WHERE id=? AND supprime=?',(rid,int(restore)))
        if not old: raise ValueError('Enregistrement indisponible.')
        if not (restore and table=='chantiers'): self.access(self.scope(table,old[0]),user,edit=True)
        with self.transaction():
            self.conn.execute(f'UPDATE {table} SET supprime=? WHERE id=?',(0 if restore else 1,rid))
            self.audit(table,rid,'restauration' if restore else 'archivage',old[0],actor)

    def grant(self,cid,uid,enabled,user):
        actor=self.actor(user,admin=True)
        self.access(cid,user)
        with self.transaction():
            self.conn.execute('DELETE FROM acces_chantiers WHERE chantier_id=? AND utilisateur_id=?',(cid,uid))
            if enabled: self.conn.execute('INSERT INTO acces_chantiers(chantier_id,utilisateur_id) VALUES(?,?)',(cid,uid))
            self.audit('acces_chantiers',cid,'attribution',{'utilisateur_id':uid,'autorise':enabled},actor)

    def photo(self,table,rid,phase,data,user):
        from PIL import Image,ImageOps
        actor=self.actor(user,edit=True)
        if table not in ('malfacons','journalier') or phase not in ('Avant','Après','Journalier'): raise ValueError('Photo invalide.')
        row=self.rows(f'SELECT * FROM {table} WHERE id=? AND supprime=0',(rid,))
        if not row: raise ValueError('Enregistrement indisponible.')
        self.access(row[0]['chantier_id'],user,edit=True)
        if len(data)>5*1024*1024: raise ValueError('Photo limitée à 5 Mo.')
        with Image.open(io.BytesIO(data)) as img:
            if img.width*img.height>20000000: raise ValueError('Photo limitée à 20 mégapixels.')
            img=ImageOps.exif_transpose(img).convert('RGB')
            img.thumbnail((1600,1600))
            out=io.BytesIO()
            img.save(out,format='JPEG',quality=85)
        with self.transaction():
            self.conn.execute('INSERT INTO photos(table_nom,row_id,chantier_id,phase,contenu,ts) VALUES(?,?,?,?,?,?)',(table,rid,row[0]['chantier_id'],phase,out.getvalue(),dt.datetime.now().isoformat()))
            self.audit(table,rid,'photo',{'phase':phase},actor)

    def summary(self,cid,user):
        self.access(cid,user)
        site=self.rows('SELECT * FROM chantiers WHERE id=?',(cid,))[0]
        total=self.rows('SELECT COALESCE(SUM(montant_fcfa),0) total FROM depenses WHERE chantier_id=? AND supprime=0',(cid,))[0]['total']
        progress=self.rows('SELECT pourcentage FROM avancement WHERE chantier_id=? AND supprime=0 ORDER BY date_saisie DESC,id DESC LIMIT 1',(cid,))
        consumed=total/site['budget_fcfa']*100 if site['budget_fcfa'] else None
        return site,total,progress[0]['pourcentage'] if progress else 0,consumed

    def backup(self):
        if self.postgres: raise ValueError('Utilisez les sauvegardes de votre fournisseur PostgreSQL.')
        return super().backup()


from pathlib import Path

import streamlit as st

LABELS = {
    'identifiant': 'Identifiant', 'nom_complet': 'Nom complet', 'role': 'Rôle',
    'actif': 'Actif', 'code': 'Code', 'nom': 'Nom', 'client': 'Client',
    'localisation': 'Localisation', 'budget_fcfa': 'Budget (FCFA)',
    'date_debut': 'Début', 'date_fin_prevue': 'Fin prévue', 'statut': 'Statut',
    'date_jour': 'Date', 'meteo': 'Météo', 'effectif': 'Effectif',
    'travaux_realises': 'Travaux réalisés', 'incidents': 'Incidents',
    'element': 'Élément', 'type_defaut': 'Défaut', 'criticite': 'Criticité',
    'description': 'Description', 'action_corrective': 'Action corrective',
    'statut_resolution': 'Résolution', 'date_signalement': 'Signalement',
    'categorie': 'Catégorie', 'libelle': 'Libellé', 'montant_fcfa': 'Montant (FCFA)',
    'date_depense': 'Date', 'reference_piece': 'Référence',
    'pourcentage': 'Avancement (%)', 'date_saisie': 'Date',
    'designation': 'Désignation', 'quantite': 'Quantité', 'unite': 'Unité',
    'date_reception': 'Réception', 'numero': 'Numéro', 'objet': 'Objet',
    'tva_pct': 'TVA (%)', 'prix_unitaire_fcfa': 'Prix unitaire (FCFA)',
}


def install_layout():
    st.html(STYLE)


def records(rows, key, title):
    """Both views share data; CSS switches views without a viewport rerun."""
    if not rows:
        st.info('Aucun enregistrement pour le moment.')
        return
    visible = [{LABELS.get(k, k): v for k, v in row.items()
                if k not in {'supprime', 'chantier_id', 'devis_id'}} for row in rows]
    with st.container(key=f'desktop_{key}'):
        st.dataframe(visible, hide_index=True, width='stretch', alt=title)
    with st.container(key=f'mobile_{key}'):
        count = max(1, (len(rows) + 9) // 10)
        page = st.selectbox('Page', range(1, count + 1), key=f'page_{key}')
        st.caption(f'{len(rows)} enregistrement(s)')
        for row in rows[(page - 1) * 10:page * 10]:
            name = next((str(row[k]) for k in ('nom', 'libelle', 'element', 'designation', 'numero', 'nom_complet', 'date_jour', 'date_saisie') if row.get(k)), str(row.get('id', 'Détail')))
            with st.expander(name):
                for field, value in row.items():
                    if field in {'supprime', 'chantier_id', 'devis_id', 'id'}:
                        continue
                    st.caption(LABELS.get(field, field))
                    st.text('—' if value is None or value == '' else str(value), width='stretch', wrap=True)


def metrics(items):
    for offset in range(0, len(items), 2):
        for column, (label, value) in zip(st.columns(2), items[offset:offset + 2]):
            with column:
                st.metric(label, value)


import datetime as dt
import io
from xml.sax.saxutils import escape

import streamlit as st


OPTIONS = {
    'statut_resolution': ['Ouvert','En cours','Résolu'],
    'criticite': ['Faible','Moyenne','Élevée','Critique'],
    'categorie': ['materiaux','main_oeuvre','materiel','sous_traitance','transport','autre'],
    'statut': ['prevu','en_cours','suspendu','termine'],
}
NUMBERS = {'budget_fcfa','montant_fcfa','quantite','prix_unitaire_fcfa','tva_pct','pourcentage','effectif'}


def action(callback):
    try:
        callback()
        st.session_state.flash = 'Modification enregistrée.'
        st.rerun()
    except Exception as exc:
        if isinstance(exc,(ValueError,OSError)):
            st.error(str(exc))
        else:
            st.error('Enregistrement impossible. Vérifiez les valeurs et les codes uniques.')


def manage(db,table,rows,user):
    if not rows or user['role'] not in ('admin','editeur'):
        return
    with st.expander('Modifier ou archiver'):
        ids={row['id']:row for row in rows}
        rid=st.selectbox('Enregistrement',list(ids),key=f'edit_id_{table}',format_func=lambda key: f"{key} - "+next((str(ids[key][k]) for k in ('nom','libelle','designation','numero','element','date_jour','date_saisie') if ids[key].get(k)), 'Détail'))
        row=ids[rid]
        with st.form(f'edit_{table}_{rid}'):
            changes={}
            for key,value in row.items():
                if key in ('id','supprime','chantier_id','devis_id'): continue
                label=LABELS.get(key,key)
                if key.startswith('date_'):
                    changes[key]=st.date_input(label,value=dt.date.fromisoformat(value)).isoformat()
                elif key in NUMBERS:
                    changes[key]=st.number_input(label,min_value=0 if key=='effectif' else 0.0,value=int(value or 0) if key=='effectif' else float(value or 0),max_value=100.0 if key in ('tva_pct','pourcentage') else None)
                elif key in OPTIONS:
                    options = ['brouillon','envoye','accepte','refuse'] if table=='devis' and key=='statut' else OPTIONS[key]
                    if value not in options: options=[value]+options
                    changes[key]=st.selectbox(label,options,index=options.index(value))
                else:
                    changes[key]=st.text_area(label,value=str(value or ''))
            if st.form_submit_button('Enregistrer les modifications',icon=':material/save:',width='stretch'):
                action(lambda:db.update(table,rid,changes,user))
        with st.form(f'archive_{table}'):
            confirm=st.checkbox('Confirmer l’archivage de cet enregistrement')
            if st.form_submit_button('Archiver',icon=':material/archive:',width='stretch'):
                if confirm: action(lambda:db.archive(table,rid,user))
                else: st.warning('Confirmez l’archivage.')


def filter_rows(rows,key):
    if not rows: return rows
    with st.expander('Recherche et filtres'):
        query=st.text_input('Rechercher',key=f'q_{key}').strip().casefold()
        fields=list(rows[0])
        date_key=next((field for field in fields if field.startswith('date_')),None)
        if date_key:
            dates=[dt.date.fromisoformat(row[date_key]) for row in rows if row.get(date_key)]
            interval=st.date_input('Période',value=(min(dates),max(dates)),key=f'dates_{key}') if dates else ()
        else: interval=()
        category=st.selectbox('Catégorie', ['Toutes']+sorted({row['categorie'] for row in rows}),key=f'cat_{key}') if 'categorie' in fields else 'Toutes'
        amount_filter=st.checkbox('Filtrer par montant',key=f'amount_{key}') if 'montant_fcfa' in fields else False
        minimum=st.number_input('Montant minimum (FCFA)',min_value=0.0,key=f'min_{key}') if amount_filter else 0
        maximum=st.number_input('Montant maximum (FCFA)',min_value=0.0,value=max(float(row['montant_fcfa']) for row in rows),key=f'max_{key}') if amount_filter else float('inf')
    result=[]
    for row in rows:
        if query and query not in ' '.join(str(v) for v in row.values()).casefold(): continue
        if category!='Toutes' and row.get('categorie')!=category: continue
        if 'montant_fcfa' in row and not minimum<=row['montant_fcfa']<=maximum: continue
        if len(interval)==2 and not interval[0]<=dt.date.fromisoformat(row[date_key])<=interval[1]: continue
        result.append(row)
    return result


def photos(db,table,rows,cid,user):
    if not rows: return
    with st.expander('Photos'):
        rid=st.selectbox('Rapport' if table=='journalier' else 'Malfaçon', [r['id'] for r in rows],key=f'photo_record_{table}')
        if user['role'] in ('admin','editeur'):
            with st.form(f'photo_{table}_{rid}'):
                phase=st.selectbox('Étape', ['Avant','Après'] if table=='malfacons' else ['Journalier'])
                upload=st.file_uploader('Photo JPG ou PNG',type=['jpg','jpeg','png'],max_upload_size=5)
                if st.form_submit_button('Ajouter la photo',icon=':material/add_a_photo:',width='stretch'):
                    if upload: action(lambda:db.photo(table,rid,phase,upload.getvalue(),user))
                    else: st.warning('Choisissez une photo.')
        db.access(cid,user)
        images=db.rows('SELECT phase,contenu,ts FROM photos WHERE table_nom=? AND row_id=? AND chantier_id=? ORDER BY id DESC',(table,rid,cid))
        for image in images:
            st.image(bytes(image['contenu']),caption=f"{image['phase']} - {image['ts'][:10]}",width='stretch',alt=f"Photo {image['phase']}")


def alerts(db,cid,user):
    site,total,progress,consumed=db.summary(cid,user)
    if consumed is not None:
        if consumed>=100: st.error(f'Budget atteint ou dépassé : {consumed:.1f} % consommé.')
        elif consumed>=80: st.warning(f'Budget presque consommé : {consumed:.1f} %.')
        if consumed-progress>=20: st.warning(f'Écart de {consumed-progress:.1f} points entre budget consommé et avancement. À examiner.')
    elif total>0: st.warning('Dépenses présentes mais budget fixé à zéro.')
    if site['date_fin_prevue']<dt.date.today().isoformat() and site['statut']!='termine': st.warning('Échéance du chantier dépassée.')
    critical=db.rows("SELECT COUNT(*) total FROM malfacons WHERE chantier_id=? AND supprime=0 AND criticite='Critique' AND statut_resolution!='Résolu'",(cid,))[0]['total']
    if critical: st.error(f'{critical} malfaçon(s) critique(s) non résolue(s).')
    st.caption(f'Avancement physique : {progress:.1f} % | Budget consommé : '+(f'{consumed:.1f} %' if consumed is not None else 'non calculable'))


def report_pdf(db,cid,user):
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,Image,KeepTogether
    styles=getSampleStyleSheet()
    out=io.BytesIO()
    story=[]
    def text(value,style='BodyText'): return Paragraph(escape(str(value)).replace('\n','<br/>'),styles[style])
    site,total,progress,consumed=db.summary(cid,user)
    story += [text('Génie civil pro - Rapport de chantier','Title'),text(site['nom'],'Heading1'),text(f"Code : {site['code']} | Client : {site['client'] or '-'}"),text(f"Période : {site['date_debut']} au {site['date_fin_prevue']}"),Spacer(1,12)]
    for label,value in [('Budget',f"{site['budget_fcfa']:,.0f} FCFA"),('Dépenses',f'{total:,.0f} FCFA'),('Avancement',f'{progress:.1f} %'),('Budget consommé',f'{consumed:.1f} %' if consumed is not None else 'Non calculable')]:
        story.append(text(f'{label} : {value}'))
    for table,title,fields in [
        ('depenses','Dépenses',['date_depense','libelle','categorie','montant_fcfa']),
        ('avancement','Avancement',['date_saisie','pourcentage','description']),
        ('journalier','Rapports journaliers',['date_jour','meteo','effectif','travaux_realises','incidents']),
        ('malfacons','Malfaçons',['element','type_defaut','criticite','statut_resolution','description','action_corrective']),
        ('materiel','Matériel',['designation','quantite','unite','date_reception']),
        ('devis','Devis',['numero','objet','statut','tva_pct'])]:
        story.append(text(title,'Heading2'))
        rows=db.rows(f'SELECT * FROM {table} WHERE chantier_id=? AND supprime=0 ORDER BY id',(cid,))
        if not rows: story.append(text('Aucun enregistrement.'))
        for row in rows:
            story.append(text(f"Enregistrement {row['id']}",'Heading3'))
            # Paragraphs can split across pages even for unusually long reports.
            for field in fields:
                value=row.get(field)
                story.append(text(f"{LABELS.get(field,field)} : {value if value is not None and value != '' else '-'}"))
            if table=='devis':
                lines=db.rows('SELECT * FROM lignes_devis WHERE devis_id=? AND supprime=0',(row['id'],))
                for line in lines:
                    story.append(text(f"{line['designation']} : {line['quantite']} {line['unite']} x {line['prix_unitaire_fcfa']:,.0f} FCFA"))
                ht=sum(line['quantite']*line['prix_unitaire_fcfa'] for line in lines)
                story.append(text(f"Total HT : {ht:,.0f} FCFA | Total TTC : {ht*(1+row['tva_pct']/100):,.0f} FCFA"))
    for table in ('malfacons','journalier'):
        for photo in db.rows(f'SELECT p.phase,p.contenu,p.row_id FROM photos p JOIN {table} m ON p.row_id=m.id WHERE p.chantier_id=? AND p.table_nom=? AND m.supprime=0 ORDER BY p.id',(cid,table)):
            img=Image(io.BytesIO(bytes(photo['contenu'])))
            scale=min(450/img.imageWidth,260/img.imageHeight)
            img.drawWidth=img.imageWidth*scale
            img.drawHeight=img.imageHeight*scale
            story.append(KeepTogether([text(f"Photo {table} {photo['row_id']} - {photo['phase']}",'Heading3'),img]))
    def footer(canvas,doc):
        canvas.setFont('Helvetica',8)
        canvas.drawString(40,25,'Génie civil pro - '+dt.date.today().isoformat())
        canvas.drawRightString(A4[0]-40,25,f'Page {doc.page}')
    SimpleDocTemplate(out,pagesize=A4,leftMargin=40,rightMargin=40,topMargin=40,bottomMargin=40).build(story,onFirstPage=footer,onLaterPages=footer)
    return out.getvalue()


def admin_access(db,cid,user):
    users=db.rows('SELECT id,identifiant,nom_complet,role FROM utilisateurs ORDER BY id')
    if not cid: st.info('Créez ou sélectionnez un chantier.'); return
    with st.form('grant'):
        uid=st.selectbox('Utilisateur',[u['id'] for u in users],format_func=lambda key: next(u['nom_complet']+' ('+u['role']+')' for u in users if u['id']==key))
        enabled=st.checkbox('Autoriser ce chantier',value=True)
        if st.form_submit_button('Appliquer l’accès',icon=':material/key:',width='stretch'):
            action(lambda:db.grant(cid,uid,enabled,user))
    records(db.rows('SELECT u.identifiant,u.nom_complet,u.role FROM utilisateurs u JOIN acces_chantiers a ON a.utilisateur_id=u.id WHERE a.chantier_id=?',(cid,)),'grants','Accès au chantier')
    st.caption('Les administrateurs ont accès à tous les chantiers. Les autres comptes accèdent uniquement aux chantiers attribués.')


def history(db,cid,user):
    if not cid: st.info('Sélectionnez un chantier.'); return
    db.access(cid,user)
    visible=[]
    for row in db.rows('SELECT * FROM historique ORDER BY id DESC'):
        table=row['table_nom']
        if table=='acces_chantiers': related=row['row_id']==cid
        elif table=='chantiers': related=row['row_id']==cid
        elif table in ('depenses','avancement','journalier','malfacons','materiel','devis','lignes_devis'):
            data=db.rows(f'SELECT * FROM {table} WHERE id=?',(row['row_id'],))
            if not data: continue
            try: related=db.scope(table,data[0])==cid
            except ValueError: related=False
        else: continue
        if related: visible.append(row)
    records(visible,'history','Historique des modifications')



STYLE = STYLE.replace('</style>', '\n[data-testid="stBaseButton-primary"] { background:#126c77 !important; border-color:#126c77 !important; color:white !important; }\n[data-testid="stBaseButton-primary"]:hover { background:#0e555e !important; }\n[data-testid="stCaptionContainer"] p { color:#5c737c !important; }\n</style>')

# This source is embedded in the delivered app.py by the packaging step.
import hashlib
import json
import math
import textwrap
from graphlib import TopologicalSorter, CycleError
import numpy as np
from scipy import stats
import plotly.graph_objects as go
from plotly.subplots import make_subplots

ANALYSIS_KINDS = ['Coûts', 'Délais', 'Matériaux', 'Poutre']
LAWS = ['Lognormale', 'Uniforme positive']
ASSUMPTIONS = {
    'Coûts': 'C = somme(Qi × Pi). Quantités et prix indépendants entre eux et entre postes. Aucun effet macroéconomique commun ni corrélation modélisé. Les valeurs P80/P95 sont des quantiles prédictifs conditionnels au modèle, pas des intervalles de confiance.',
    'Délais': 'Planning acyclique, tâches non préemptives, débuts au plus tôt, ressources illimitées. Durées indépendantes. Chaque tâche commence après la fin de tous ses prédécesseurs ; les branches parallèles ne sont pas additionnées.',
    'Matériaux': 'Échantillon supposé représentatif, observations indépendantes et strictement positives. Le seuil est choisi par l’utilisateur, sans qualification réglementaire. Une loi lognormale ajustée est une hypothèse, pas un fait démontré.',
    'Poutre': 'Poutre droite rectangulaire pleine en matériau élastique homogène ; deux appuis simples, charge centrale P et charge uniforme q. Euler-Bernoulli, petites déformations. Pas de poids propre automatique, de fissuration, de flambement, de déversement ni de vérification normative. Variables indépendantes. Un dépassement simulé n’est pas une probabilité universelle de rupture.',
}
REFERENCES = [
    ('SymPy : poutres', 'https://docs.sympy.org/latest/modules/physics/continuum_mechanics/beam.html'),
    ('SciPy : intervalle binomial exact', 'https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html'),
    ('SciPy : corrélation de Spearman', 'https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html'),
]


def finite_number(value, label, low=0, strict=False, high=None):
    if isinstance(value, bool) or not isinstance(value, (int,float)): raise ValueError(label + ' : nombre attendu.')
    try: value = float(value)
    except (TypeError, ValueError): raise ValueError(label + ' : nombre attendu.')
    if not math.isfinite(value) or (value <= low if strict else value < low) or (high is not None and value > high):
        raise ValueError(label + ' : valeur hors limites.')
    return value


def validate_analysis(c):
    if not isinstance(c, dict) or c.get('kind') not in ANALYSIS_KINDS: raise ValueError('Analyse inconnue.')
    if c.get('law') not in LAWS: raise ValueError('Loi inconnue.')
    for key, lo, hi in [('n',1000,100000),('seed',0,2147483647)]:
        if isinstance(c.get(key), bool) or not isinstance(c.get(key), int) or not lo<=c[key]<=hi: raise ValueError(key + ' invalide.')
    k = c['kind']
    if k in ('Coûts','Délais'):
        rows=c.get('rows')
        if not isinstance(rows,list) or not 1<=len(rows)<=50: raise ValueError('Entre 1 et 50 lignes attendues.')
        finite_number(c.get('limit'),'Budget / échéance',strict=True)
        for row in rows:
            if not isinstance(row,dict): raise ValueError('Ligne invalide.')
            keys = ['quantite','prix'] if k=='Coûts' else ['duree']
            for name in keys:
                finite_number(row.get(name),name,strict=True)
                finite_number(row.get('cv_'+name),'CV '+name,high=.5)
        if k=='Délais': planning_order(rows)
    elif k=='Matériaux':
        vals=c.get('values')
        if not isinstance(vals,list) or not 3<=len(vals)<=20000: raise ValueError('Entre 3 et 20 000 essais attendus.')
        for v in vals: finite_number(v,'Résultat d’essai',strict=True)
        finite_number(c.get('limit'),'Seuil',strict=True)
        if not isinstance(c.get('unit'),str) or not 1<=len(c['unit'])<=30: raise ValueError('Unité attendue (30 caractères maximum).')
    else:
        for name in ('L','b','h','E','fy','ratio'):
            finite_number(c.get(name),name,strict=True)
        for name in ('P','q'): finite_number(c.get(name),name)
        for name in ('P','q','b','h','fy'): finite_number(c.get('cv_'+name),'CV '+name,high=.5)
    return c


def planning_order(rows):
    ids=[str(r.get('id','')).strip() for r in rows]
    if any(not i or len(i)>30 for i in ids) or len(set(ids))!=len(ids): raise ValueError('Identifiants de tâches uniques requis.')
    deps={i:[x.strip() for x in str(r.get('predecesseurs','')).split(',') if x.strip()] for i,r in zip(ids,rows)}
    if any(p not in ids for values in deps.values() for p in values): raise ValueError('Prédécesseur inconnu.')
    try: order=list(TopologicalSorter(deps).static_order())
    except CycleError: raise ValueError('Cycle détecté dans le planning.')
    return order,deps


def draw_positive(rng, mean, cv, n, law):
    z=rng.standard_normal(n)
    if cv==0 or mean==0: return np.full(n,mean,dtype=float)
    if law=='Lognormale':
        sigma=np.sqrt(np.log1p(cv*cv))
        return mean*np.exp(sigma*z-sigma*sigma/2)
    return mean*(1+np.sqrt(3)*cv*(2*stats.norm.cdf(z)-1))


def exact_probability(mask):
    n=len(mask); count=int(np.count_nonzero(mask))
    ci=stats.binomtest(count,n).proportion_ci(confidence_level=.95,method='exact')
    return dict(p=count/n,low=float(ci.low),high=float(ci.high),count=count,n=n)


@st.cache_resource
def beam_influences():
    import sympy as sp
    from sympy.physics.continuum_mechanics.beam import Beam
    x=sp.Symbol('x',real=True)
    output=[]
    for uniform in (False,True):
        beam=Beam(1,1,1,variable=x)
        ra=beam.apply_support(0,'pin'); rb=beam.apply_support(1,'roller')
        beam.apply_load(-1,0,0,end=1) if uniform else beam.apply_load(-1,sp.Rational(1,2),-1)
        beam.solve_for_reaction_loads(ra,rb)
        output.append({name:sp.lambdify(x,expr.rewrite(sp.Piecewise),'numpy') for name,expr in [('V',beam.shear_force()),('M',beam.bending_moment()),('y',beam.deflection())]})
    return output


def beam_nominal(c):
    length=c['L']; b=c['b']/1000; h=c['h']/1000
    inertia=b*h**3/12; section=b*h*h/6
    moment=c['P']*1000*length/4+c['q']*1000*length*length/8
    stress=moment/section/1e6
    deflection=(c['P']*1000*length**3/48+5*c['q']*1000*length**4/384)/(c['E']*1e9*inertia)*1000
    return dict(M=moment/1000,sigma=stress,delta=deflection,I=inertia,W=section)


@st.cache_data(ttl=1800,max_entries=6)
def compute_analysis(serialized):
    c=validate_analysis(json.loads(serialized)); k=c['kind']; n=c['n']; rng=np.random.default_rng(c['seed']); inputs={}
    if k=='Coûts':
        values=np.zeros(n)
        for i,r in enumerate(c['rows']):
            quantity=draw_positive(rng,float(r['quantite']),float(r['cv_quantite']),n,c['law'])
            price=draw_positive(rng,float(r['prix']),float(r['cv_prix']),n,c['law'])
            values+=quantity*price
            inputs[f'Quantité {i+1}']=quantity; inputs[f'Prix {i+1}']=price
        mask=values>c['limit']; unit='FCFA'; label='Coût total'; limit=c['limit']
    elif k=='Délais':
        order,deps=planning_order(c['rows']); rows={str(r['id']).strip():r for r in c['rows']}; ends={}
        for task in order:
            r=rows[task]; duration=draw_positive(rng,float(r['duree']),float(r['cv_duree']),n,c['law'])
            start=np.maximum.reduce([ends[p] for p in deps[task]]) if deps[task] else np.zeros(n)
            ends[task]=start+duration; inputs[task]=duration
        values=np.maximum.reduce(list(ends.values())); mask=values>c['limit']; unit='jours'; label='Durée du projet'; limit=c['limit']
    elif k=='Matériaux':
        values=np.asarray(c['values'],dtype=float); mask=values<c['limit']; unit=c['unit']; label='Résultat d’essai'; limit=c['limit']
    else:
        for name in ('P','q','b','h','fy'): inputs[name]=draw_positive(rng,float(c[name]),float(c['cv_'+name]),n,c['law'])
        moment=inputs['P']*1000*c['L']/4+inputs['q']*1000*c['L']**2/8
        section=(inputs['b']/1000)*(inputs['h']/1000)**2/6
        values=inputs['fy']-moment/section/1e6
        mask=values<0; unit='MPa'; label='Marge g = fy − σ'; limit=0
    if not np.all(np.isfinite(values)): raise ValueError('Résultats non finis : vérifiez les ordres de grandeur.')
    risk=exact_probability(mask)
    checkpoints=np.unique(np.linspace(min(20,len(values)),len(values),45,dtype=int)); cumulative=np.cumsum(mask)
    sensitivity=[]
    if np.ptp(values)>0:
        for name,arr in inputs.items():
            if np.ptp(arr)>0:
                rho=float(stats.spearmanr(arr,values).statistic)
                if math.isfinite(rho): sensitivity.append((name,rho))
    result=dict(values=values,mask=mask,risk=risk,unit=unit,label=label,limit=limit,sensitivity=sensitivity,inputs=inputs,
                convergence=[(int(i),float(cumulative[i-1]/i)) for i in checkpoints],config=c)
    if k=='Matériaux':
        logs=np.log(values); sd=float(np.std(logs,ddof=0)); mu=float(np.mean(logs))
        result['fitted_p']=float(stats.norm.cdf((math.log(limit)-mu)/sd)) if sd>1e-12 else None
    return result


def chart_style(fig,title,xlabel,ylabel,height=360):
    title_lines=textwrap.wrap(title,width=28)
    fig.update_layout(title=dict(text='<br>'.join(title_lines),font=dict(size=14)),template='plotly_white',height=height,
                      margin=dict(l=16,r=16,t=35+20*len(title_lines),b=65),font=dict(size=12,color='#23333b'),
                      paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='#f4f8fa',showlegend=False)
    fig.update_xaxes(title=xlabel,automargin=True); fig.update_yaxes(title=ylabel,automargin=True)
    return fig


def result_charts(r):
    vals=r['values']; unit=r['unit']; xlabel=r['label']+' ('+unit+')'
    hist=go.Figure(go.Histogram(x=vals,nbinsx=45,marker_color='#177e89',name='Observations'))
    hist.add_vline(x=r['limit'],line_color='#c84c50',line_dash='dash',name='Seuil',showlegend=True)
    for quantile,color,name in [(.8,'#af7413','P80'),(.95,'#5577a4','P95')]:
        hist.add_vline(x=float(np.quantile(vals,quantile)),line_color=color,line_dash='dot',name=name,showlegend=True)
    cdf=go.Figure(go.Scatter(x=np.sort(vals)[::max(1,len(vals)//2000)],y=np.arange(1,len(vals)+1)[::max(1,len(vals)//2000)]/len(vals),line=dict(color='#177e89')))
    cdf.add_vline(x=r['limit'],line_color='#c84c50',line_dash='dash')
    conv=go.Figure(go.Scatter(x=[x for x,y in r['convergence']],y=[100*y for x,y in r['convergence']],line=dict(color='#af7413')))
    charts=[chart_style(hist,'Distribution et seuil',xlabel,'Effectif'),chart_style(cdf,'Répartition empirique',xlabel,'Fréquence cumulée'),chart_style(conv,'Fréquence cumulée selon le nombre d’observations' if r['config']['kind']=='Matériaux' else 'Convergence Monte-Carlo','Observations' if r['config']['kind']=='Matériaux' else 'Tirages','Fréquence (%)')]
    charts[0].update_layout(showlegend=True,height=420,legend=dict(orientation='h',y=-.35,yanchor='top',x=0,font=dict(size=10)),margin=dict(b=110))
    if r['sensitivity']:
        rows=sorted(r['sensitivity'],key=lambda v:abs(v[1]))
        sens=go.Figure(go.Bar(x=[v for _,v in rows],y=[key for key,_ in rows],orientation='h',marker_color='#5577a4'))
        sens.update_xaxes(range=[-1,1]); charts.append(chart_style(sens,'Sensibilité exploratoire','Corrélation de Spearman','Variable',max(330,min(1000,25*len(rows)+120))))
    return charts


def beam_charts(c):
    length=c['L']; u=np.linspace(0,1,201); point,uniform=beam_influences()
    P=c['P']*1000; q=c['q']*1000; ei=c['E']*1e9*beam_nominal(c)['I']
    curves={name:(P*length**a*np.asarray(point[name](u))+q*length**(a+1)*np.asarray(uniform[name](u))) for name,a in [('V',0),('M',1),('y',3)]}
    # Downward loading is negative; display sagging moment positive, deflection downward.
    curves['M']=-curves['M']/1000; curves['V']=-curves['V']/1000; curves['y']=-np.abs(curves['y']/ei)*1000
    schematic=go.Figure(go.Scatter(x=[0,length],y=[0,0],mode='lines',line=dict(width=9,color='#23333b')))
    schematic.add_trace(go.Scatter(x=[0,length],y=[-.08,-.08],mode='markers',marker=dict(symbol='triangle-up',size=18,color='#23333b')))
    if P:
        schematic.add_annotation(x=length/2,y=.02,ax=length/2,ay=.7,axref='x',ayref='y',text=f'P = {c["P"]:g} kN',showarrow=True,arrowhead=2,arrowcolor='#c84c50')
    if q:
        for pos in np.linspace(.05*length,.95*length,8):
            schematic.add_annotation(x=pos,y=.03,ax=pos,ay=.35,axref='x',ayref='y',text='',showarrow=True,arrowhead=2,arrowcolor='#af7413')
        schematic.add_annotation(x=0,y=.55,text=f'q = {c["q"]:g} kN/m',showarrow=False,xanchor='left')
    schematic.update_yaxes(range=[-.25,1],visible=False)
    schematic.update_xaxes(range=[-.1*length,1.1*length])
    output=[chart_style(schematic,'Chargement et appuis simples','Position x (m)','',300)]
    section=go.Figure(go.Scatter(x=[0,c['b'],c['b'],0,0],y=[0,0,c['h'],c['h'],0],mode='lines',fill='toself',fillcolor='#dceef0',line=dict(color='#177e89',width=3)))
    section.add_trace(go.Scatter(x=[-c['b']*.2,c['b']*1.2],y=[c['h']/2]*2,mode='lines',line=dict(dash='dash',color='#5577a4')))
    section.add_trace(go.Scatter(x=[c['b']/2]*2,y=[-c['h']*.15,c['h']*1.15],mode='lines',line=dict(dash='dash',color='#5577a4')))
    section.update_yaxes(scaleanchor='x',scaleratio=1)
    output.append(chart_style(section,'Section pleine et axes centroidaux','Largeur b (mm)','Hauteur h (mm)',300))
    for key,title,unit in [('V','Effort tranchant','kN'),('M','Moment fléchissant','kN·m'),('y','Déformée élastique (réelle, non amplifiée)','mm')]:
        fig=go.Figure(go.Scatter(x=u*length,y=curves[key],mode='lines',fill='tozeroy',line=dict(color='#177e89')))
        output.append(chart_style(fig,title,'Position x (m)',unit,300))
    return output


def analysis_pdf(r):
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib.figure import Figure
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    from xml.sax.saxutils import escape
    out=io.BytesIO(); styles=getSampleStyleSheet(); story=[]
    def p(s,style='BodyText'):
        s=str(s).replace('σ','sigma').replace('−','-')
        return Paragraph(escape(s),styles[style])
    c=r['config']; risk=r['risk']
    story.extend([p('Génie Civil Pro — Analyse probabiliste','Title'),p(c['kind'],'Heading1'),p('Provenance : '+c.get('origin','Données saisies')),p(ASSUMPTIONS[c['kind']]),Spacer(1,10)])
    story.append(p(f"Événements : {risk['count']} / {risk['n']} ; fréquence {risk['p']:.3%} ; IC binomial exact 95 % [{risk['low']:.3%} ; {risk['high']:.3%}]."))
    story.append(p('L’IC quantifie l’incertitude d’échantillonnage, pas l’erreur du modèle. Zéro événement ne signifie pas risque nul.'))
    story.append(p('Paramètres et hypothèses','Heading2'))
    for key,val in c.items():
        if key in ('rows','values'): continue
        story.append(p(f'{key} : {val}'))
    if 'rows' in c:
        for row in c['rows']: story.append(p(' | '.join(f'{key} : {value}' for key,value in row.items())))
    if 'values' in c:
        story.append(p(f"Essais : {len(c['values'])}, données complètes disponibles dans le JSON de l’étude."))
    story.append(p('Résultats et quantiles prédictifs conditionnels','Heading2'))
    story.append(p(f"Moyenne : {np.mean(r['values']):.4g} {r['unit']} ; P50/P80/P95 : {np.quantile(r['values'],[.5,.8,.95])} {r['unit']}"))
    if c['kind']=='Matériaux': story.append(p(f"Probabilité sous le seuil, modèle lognormal ajusté : {r.get('fitted_p')} (sans intervalle de confiance d’ajustement)."))
    def image_figure(fig):
        buf=io.BytesIO(); fig.savefig(buf,format='png',dpi=145,bbox_inches='tight');buf.seek(0)
        story.append(Image(buf,width=475,height=245));story.append(Spacer(1,8))
    fig=Figure(figsize=(8,4));ax=fig.subplots();ax.hist(r['values'],bins=35,color='#177e89');ax.axvline(r['limit'],color='#c84c50',linestyle='--');ax.set(xlabel=r['label']+' ('+r['unit']+')',ylabel='Effectif',title='Distribution et seuil');image_figure(fig)
    fig=Figure(figsize=(8,4));ax=fig.subplots();ax.plot(*zip(*r['convergence']),color='#af7413');ax.set(xlabel='Observations / tirages',ylabel='Fréquence cumulée',title='Convergence');image_figure(fig)
    if r['sensitivity']:
        rows=sorted(r['sensitivity'],key=lambda x:abs(x[1]),reverse=True)[:12]
        fig=Figure(figsize=(8,4));ax=fig.subplots();ax.barh([k for k,v in rows],[v for k,v in rows],color='#5577a4');ax.set(xlim=(-1,1),xlabel='Spearman',title='Sensibilité exploratoire (12 variables maximum)');image_figure(fig)
        story.append(p('Les corrélations de rang ne sont ni des causalités ni des contributions additives au risque.'))
    if c['kind']=='Poutre':
        story.append(p('Mécanique nominale : '+str(beam_nominal(c))))
        for diagram in beam_charts(c):
            if len(diagram.data[0].x)>20:
                fig=Figure(figsize=(8,4));ax=fig.subplots();ax.plot(diagram.data[0].x,diagram.data[0].y,color='#177e89');ax.set(xlabel='Position x (m)',ylabel=diagram.layout.yaxis.title.text,title=diagram.layout.title.text.replace('<br>','\n'));image_figure(fig)
        story.append(p('g = fy − M/W en MPa ; I = bh³/12 ; W = bh²/6 ; Mmax = PL/4 + qL²/8.'))
    story.append(p('Sources','Heading2'))
    for name,url in REFERENCES: story.append(p(name+' : '+url))
    def footer(canvas,doc):
        canvas.setFont('Helvetica',8);canvas.drawString(40,24,'Génie Civil Pro — Étude conditionnelle, non réglementaire');canvas.drawRightString(555,24,str(doc.page))
    SimpleDocTemplate(out,leftMargin=40,rightMargin=40,topMargin=40,bottomMargin=40).build(story,onFirstPage=footer,onLaterPages=footer)
    return out.getvalue()


def default_analysis(kind):
    common=dict(kind=kind,n=10000,seed=42,law=LAWS[0],origin='Exemple pédagogique fictif — à remplacer')
    if kind=='Coûts': return dict(common,limit=15000000,rows=[dict(poste='Béton',quantite=100.,prix=95000.,cv_quantite=.1,cv_prix=.15),dict(poste='Acier',quantite=4.,prix=800000.,cv_quantite=.1,cv_prix=.2)])
    if kind=='Délais': return dict(common,limit=45.,rows=[dict(id='A',tache='Fondations',predecesseurs='',duree=15.,cv_duree=.2),dict(id='B',tache='Structure',predecesseurs='A',duree=20.,cv_duree=.15),dict(id='C',tache='Approvisionnement',predecesseurs='',duree=25.,cv_duree=.25),dict(id='D',tache='Assemblage',predecesseurs='B,C',duree=8.,cv_duree=.1)])
    if kind=='Matériaux': return dict(common,limit=25.,unit='MPa',values=[24.,28.,31.,26.,29.,33.,25.,30.,32.,27.])
    return dict(common,L=4.,b=100.,h=160.,E=210.,fy=235.,P=65.,q=0.,ratio=300.,cv_P=.2,cv_q=.1,cv_b=.02,cv_h=.02,cv_fy=.1)


def canonical(c): return json.dumps(c,sort_keys=True,ensure_ascii=False,allow_nan=False)


def analysis_workspace(db,cid,user):
    db.access(cid,user)
    scope=f'{user["id"]}:{cid}'
    # Keep studies scoped by account and chantier, including after logout/login.
    if st.session_state.get('analysis_scope')!=scope:
        for key in list(st.session_state):
            if key.startswith('ana_'): del st.session_state[key]
        st.session_state.analysis_scope=scope
    st.caption('ÉTUDES CONDITIONNELLES · HYPOTHÈSES EXPLICITES')
    kind=st.selectbox('Analyse',ANALYSIS_KINDS,key='ana_kind')
    base=st.session_state.get('ana_loaded',{}).get(kind,default_analysis(kind))
    with st.expander('Importer une étude JSON'):
        upload=st.file_uploader('Étude complète',type=['json'],max_upload_size=2,key='ana_import')
        if st.button('Charger les paramètres',icon=':material/upload:') and upload:
            try:
                imported=validate_analysis(json.loads(upload.getvalue()))
                st.session_state.setdefault('ana_loaded',{})[imported['kind']]=imported
                for key in list(st.session_state):
                    if key.startswith('ana_param_') or key.startswith('ana_editor_'): del st.session_state[key]
                st.session_state.ana_notice='Étude importée : sélectionner '+imported['kind']+'.'
                st.rerun()
            except (ValueError,TypeError,KeyError) as exc: st.error(str(exc))
    if 'ana_notice' in st.session_state: st.info(st.session_state.pop('ana_notice'))
    st.info(base.get('origin','Données saisies'))
    c=dict(base)
    c['origin']=st.text_input('Provenance des données',value=base.get('origin','Données saisies'),max_chars=160,key='ana_param_origin_'+kind)
    if kind!='Matériaux':
        col1,col2=st.columns(2)
        c['n']=int(col1.number_input('Nombre de tirages',min_value=1000,max_value=100000,value=base['n'],step=1000,key='ana_param_n_'+kind))
        c['seed']=int(col2.number_input('Graine aléatoire',min_value=0,max_value=2147483647,value=base['seed'],key='ana_param_seed_'+kind))
        c['law']=st.selectbox('Loi des variables positives',LAWS,index=LAWS.index(base['law']),key='ana_param_law_'+kind)
        st.caption('CV = écart-type / moyenne, saisi entre 0 et 0,50. CV nul : variable déterministe. Les lois uniformes restent positives sur cette plage.')
    else:
        st.caption('Tous les essais sont utilisés. Pas de simulation ni de graine pour cette analyse. L’ajustement paramétrique proposé est lognormal.')
    if kind in ('Coûts','Délais'):
        st.caption('Coûts en FCFA.' if kind=='Coûts' else 'Durées en jours ; prédécesseurs séparés par des virgules. Les identifiants doivent être uniques.')
        table=st.data_editor(pd.DataFrame(base['rows']),num_rows='dynamic',hide_index=True,key='ana_editor_'+kind,width='stretch')
        c['rows']=table.to_dict('records')
        c['limit']=st.number_input('Budget cible (FCFA)' if kind=='Coûts' else 'Échéance après début (jours)',min_value=.01,value=float(base['limit']),key='ana_param_limit_'+kind)
        if kind=='Délais':
            try:
                order,deps=planning_order(c['rows'])
                levels={}; positions={}; counts={}
                for task in order:
                    level=max([levels[p]+1 for p in deps[task]],default=0)
                    levels[task]=level;offset=counts.get(level,0);counts[level]=offset+1;positions[task]=(level,offset)
                graph=go.Figure()
                for task in order:
                    x,y=positions[task]
                    for pred in deps[task]:
                        px,py=positions[pred];graph.add_annotation(x=x,y=y,ax=px,ay=py,axref='x',ayref='y',text='',showarrow=True,arrowhead=2,arrowcolor='#8ca6af')
                graph.add_trace(go.Scatter(x=[positions[t][0] for t in order],y=[positions[t][1] for t in order],text=order,mode='markers+text',textposition='top center',marker=dict(size=18,color='#177e89')))
                st.plotly_chart(chart_style(graph,'Dépendances du planning','Niveau de dépendance','Branche',300),key='ana_planning_graph',width='stretch')
            except ValueError as exc: st.warning(str(exc))
    elif kind=='Matériaux':
        file=st.file_uploader('Résultats CSV ou Excel',type=['csv','xlsx'],max_upload_size=5,key='ana_material_file')
        if file:
            try:
                frame=pd.read_csv(file) if file.name.lower().endswith('.csv') else pd.read_excel(file)
                if len(frame)>20000: raise ValueError('Maximum 20 000 essais.')
                column=st.selectbox('Colonne de mesure',list(frame.columns),key='ana_material_column')
                numeric=pd.to_numeric(frame[column],errors='raise')
                if numeric.isna().any(): raise ValueError('Valeurs manquantes : nettoyer le fichier avant calcul.')
                c['values']=numeric.astype(float).tolist();c['origin']='Fichier importé : '+file.name
                st.dataframe(frame.head(20),hide_index=True,width='stretch')
            except Exception as exc:
                st.error('Import impossible : '+str(exc)); return
        else:
            text=st.text_area('Mesures (une par ligne ou séparées par ;)',value='\n'.join(map(str,base['values'])),key='ana_param_values')
            try: c['values']=[float(v.strip().replace(',','.')) for v in text.replace(';','\n').splitlines() if v.strip()]
            except ValueError: st.error('Mesures numériques attendues.'); return
        c['unit']=st.text_input('Unité des essais',value=base['unit'],max_chars=30,key='ana_param_unit')
        c['limit']=st.number_input('Seuil inférieur choisi',min_value=.001,value=float(base['limit']),key='ana_param_limit_Matériaux')
    else:
        names={'L':'Portée L (m)','b':'Largeur b (mm)','h':'Hauteur h (mm)','E':'Module E (GPa)','fy':'Résistance fy (MPa)','P':'Charge centrale P (kN)','q':'Charge répartie q (kN/m)','ratio':'Limite de flèche L /'}
        cols=st.columns(2)
        for i,(key,label) in enumerate(names.items()):
            c[key]=cols[i%2].number_input(label,min_value=0. if key in ('P','q') else .001,value=float(base[key]),key='ana_param_'+key)
        with st.expander('Incertitudes de la poutre'):
            for name in ('P','q','b','h','fy'): c['cv_'+name]=st.number_input('CV '+name,min_value=0.,max_value=.5,value=float(base['cv_'+name]),key='ana_param_cv_'+name)
        try:
            validate_analysis(c)
            nominal=beam_nominal(c)
            metrics([('Moment max.',f'{nominal["M"]:.2f} kN·m'),('Contrainte max.',f'{nominal["sigma"]:.2f} MPa'),('Flèche élastique',f'{nominal["delta"]:.2f} mm'),('Limite choisie',f'{c["L"]*1000/c["ratio"]:.2f} mm')])
            for i,fig in enumerate(beam_charts(c)): st.plotly_chart(fig,key='ana_beam_'+str(i),width='stretch')
            if nominal['sigma']>c['fy']: st.warning('Résistance nominale dépassée : la déformée élastique est une extrapolation hors domaine du matériau.')
        except (ValueError,OverflowError,ZeroDivisionError) as exc: st.error(str(exc)); return
    with st.expander('Hypothèses, équations et sources'):
        st.write(ASSUMPTIONS[kind])
        st.latex({'Coûts':r'C=\sum_i Q_iP_i', 'Délais':r'T_i=D_i+\max_{j\in Pred(i)}T_j,\quad T=\max_i T_i', 'Matériaux':r'\hat p=\frac{1}{n}\sum_i 1_{X_i<s}', 'Poutre':r'g=f_y-\frac{M}{W},\quad M=\frac{PL}{4}+\frac{qL^2}{8},\quad W=\frac{bh^2}{6},\quad I=\frac{bh^3}{12}'}[kind])
        for name,url in REFERENCES: st.markdown(f'[{name}]({url})')
        st.caption('Flèche nominale : PL³/(48EI) + 5qL⁴/(384EI). La probabilité de la poutre porte uniquement sur g < 0, pas sur la limite de flèche.')
    try: validate_analysis(c); serialized=canonical(c)
    except (ValueError,TypeError,KeyError) as exc: st.error(str(exc)); return
    fingerprint=hashlib.sha256(serialized.encode()).hexdigest()
    if st.button('Calculer l’analyse',icon=':material/calculate:',type='primary',key='ana_calculate'):
        try:
            with st.spinner('Calcul en cours…'): result=compute_analysis(serialized)
            st.session_state.ana_result=(fingerprint,result)
            st.session_state.pop('ana_pdf',None)
        except (ValueError,OverflowError,ZeroDivisionError) as exc: st.error(str(exc))
    stored=st.session_state.get('ana_result')
    if not stored: return
    if stored[0]!=fingerprint:
        st.warning('Paramètres modifiés : relancez le calcul pour actualiser les résultats et les exports.'); return
    r=stored[1]; vals=r['values']; risk=r['risk']
    st.subheader('Résultats de l’étude')
    event='Proportion observée sous le seuil' if kind=='Matériaux' else 'P(g < 0), estimation' if kind=='Poutre' else 'Probabilité de dépassement, estimation'
    metrics([(event,f'{100*risk["p"]:.2f} %'),('Moyenne',f'{np.mean(vals):,.2f} {r["unit"]}'),('P80',f'{np.quantile(vals,.8):,.2f} {r["unit"]}'),('P95',f'{np.quantile(vals,.95):,.2f} {r["unit"]}')])
    st.write(f'IC binomial exact 95 % : [{100*risk["low"]:.3f} % ; {100*risk["high"]:.3f} %] · {risk["count"]} événements / {risk["n"]} observations.')
    st.caption('L’intervalle de confiance concerne l’échantillonnage, pas la validité des hypothèses. P80/P95 sont des quantiles prédictifs conditionnels. Zéro événement observé ne signifie pas risque nul.')
    st.write(f'Médiane : {np.median(vals):,.3g} {r["unit"]} · Écart-type observé : {np.std(vals,ddof=1):,.3g} {r["unit"]}')
    if kind=='Matériaux':
        st.write('Probabilité sous le seuil selon la loi lognormale ajustée : '+(f'{r["fitted_p"]:.2%}' if r['fitted_p'] is not None else 'non identifiable : observations constantes.'))
        st.caption('Estimation paramétrique distincte de la fréquence observée ; l’incertitude de l’ajustement n’est pas quantifiée ici.')
    for i,fig in enumerate(result_charts(r)): st.plotly_chart(fig,key='ana_result_chart_'+str(i),width='stretch')
    if r['sensitivity']: st.caption('Spearman mesure une association monotone au résultat. Ce n’est ni une causalité ni une contribution additive au risque.')
    st.subheader('Scénarios et exports')
    if st.button('Mémoriser comme scénario B',icon=':material/bookmark:',key='ana_snapshot'):
        st.session_state.ana_comparison=r
    other=st.session_state.get('ana_comparison')
    if other and other['config']['kind']==kind and other['unit']==r['unit']:
        st.dataframe([dict(Scénario=label,Moyenne=float(np.mean(item['values'])),P95=float(np.quantile(item['values'],.95)),Fréquence=item['risk']['p'],Unité=item['unit']) for label,item in [('A · actif',r),('B · mémorisé',other)]],hide_index=True,width='stretch')
        fig=go.Figure()
        for label,item,color in [('A',r,'#177e89'),('B',other,'#af7413')]:
            data=np.sort(item['values']);stride=max(1,len(data)//1500)
            fig.add_trace(go.Scatter(x=data[::stride],y=np.arange(1,len(data)+1)[::stride]/len(data),name=label,line=dict(color=color)))
        fig=chart_style(fig,'Comparaison des répartitions',r['unit'],'Fréquence cumulée');fig.update_layout(showlegend=True)
        st.plotly_chart(fig,width='stretch')
        st.download_button('Paramètres du scénario B',canonical(other['config']).encode(),file_name='scenario-B.json',mime='application/json',icon=':material/download:')
    st.caption('Scénarios conservés dans la session de ce compte et chantier. Téléchargez le JSON pour les conserver durablement puis les réimporter.')
    st.download_button('Enregistrer l’étude JSON',serialized.encode(),file_name='etude-'+kind+'.json',mime='application/json',icon=':material/download:')
    csv=pd.DataFrame({r['label']+' ('+r['unit']+')':vals,'evenement':r['mask'].astype(int),**r['inputs']}).to_csv(index=False).encode('utf-8-sig')
    st.download_button('Résultats CSV',csv,file_name='resultats.csv',mime='text/csv',icon=':material/download:')
    if st.button('Préparer le PDF de l’analyse',icon=':material/picture_as_pdf:'):
        st.session_state.ana_pdf=(fingerprint,analysis_pdf(r))
    if st.session_state.get('ana_pdf',(None,))[0]==fingerprint:
        st.download_button('Télécharger le PDF de l’analyse',st.session_state.ana_pdf[1],file_name='analyse.pdf',mime='application/pdf',icon=':material/download:')


def report_with_analysis(db,cid,user):
    from pypdf import PdfReader, PdfWriter
    db.access(cid,user)
    writer=PdfWriter()
    writer.append(PdfReader(io.BytesIO(report_pdf(db,cid,user))))
    stored=st.session_state.get('ana_result')
    if stored and st.session_state.get('analysis_scope')==f'{user["id"]}:{cid}':
        writer.append(PdfReader(io.BytesIO(analysis_pdf(stored[1]))))
    output=io.BytesIO();writer.write(output)
    return output.getvalue()

STYLE = STYLE.replace('</style>', '''
.stApp { background:#f5f7fb; }
[data-testid="stSidebar"] { background:#fff; border-right:1px solid #e2e7ef; }
[data-testid="stSidebar"] h3 { color:#2563ba; }
[data-testid="stMainBlockContainer"] { max-width:1480px; }
h1 { font-size:2rem !important; }
[data-testid="stBaseButton-primary"], [data-testid="stFormSubmitButton"] button { background:#2563ba !important; border-color:#2563ba !important; }
[data-testid="stBaseButton-primary"]:hover { background:#1b4c93 !important; }
[class*="st-key-dash_kpi_"] { background:#fff; border:1px solid #e2e7ef; border-radius:8px; padding:18px; min-height:150px; }
[class*="st-key-dash_kpi_"] [data-testid="stMetric"] { border:0; padding:0; }
.st-key-dash_kpi_budget { background:#eaf1ff; border-top:4px solid #3679d8; }
.st-key-dash_kpi_spent { background:#fff3e4; border-top:4px solid #d89021; }
.st-key-dash_kpi_progress { background:#e5f5ef; border-top:4px solid #22865e; }
.st-key-dash_kpi_quality { background:#fcecef; border-top:4px solid #c74c6a; }
.st-key-dash_kpi_budget [data-testid="stMetricValue"] { color:#245eac; }
.st-key-dash_kpi_spent [data-testid="stMetricValue"] { color:#995c09; }
.st-key-dash_kpi_progress [data-testid="stMetricValue"] { color:#19704c; }
.st-key-dash_kpi_quality [data-testid="stMetricValue"] { color:#ad3653; }
[class*="st-key-dash_action_"] button { min-height:50px; width:100%; border:1px solid #d6dfef; background:white; font-weight:600; }
.st-key-dash_action_cost button { color:#995c09; background:#fff3e4; border-color:#f0d29e; }
.st-key-dash_action_quality button { color:#ad3653; background:#fcecef; border-color:#efc4ce; }
.st-key-dash_action_analysis button { color:#245eac; background:#eaf1ff; border-color:#bbd1f2; }
.st-key-dash_action_daily button { color:#19704c; background:#e5f5ef; border-color:#b9dfce; }
[data-testid="stCaptionContainer"] { color:#607185; }
@media(max-width:640px) {
 [class*="st-key-dash_kpi_"] { min-height:132px; padding:14px; }
}
</style>''')


def dashboard_route(domain, section):
    st.session_state.domain = domain
    st.session_state.section = section


def dashboard(db, cid, user):
    db.access(cid, user)
    site, spent, progress, consumed = db.summary(cid, user)
    defects = db.rows("SELECT COUNT(*) total FROM malfacons WHERE chantier_id=? AND supprime=0 AND statut_resolution!='Résolu'", (cid,))[0]['total']
    has_progress = bool(db.rows('SELECT id FROM avancement WHERE chantier_id=? AND supprime=0 LIMIT 1', (cid,)))
    budget = float(site['budget_fcfa'])
    remaining = budget - spent
    st.badge(STATUT_LABELS.get(site['statut'], site['statut']), color='green' if site['statut']=='termine' else 'blue')
    st.write(f"**{site['nom']}** · {site.get('localisation') or 'Localisation non renseignée'}")
    columns = st.columns(4)
    values = [
        ('budget', 'account_balance_wallet', 'Budget du chantier', f'{budget:,.0f}', 'FCFA · enveloppe prévue'),
        ('spent', 'payments', 'Dépenses engagées', f'{spent:,.0f}', f'{consumed:.1f} % du budget' if consumed is not None else 'Budget non défini'),
        ('progress', 'trending_up', 'Avancement physique', f'{progress:.1f} %' if has_progress else '—', 'Dernière saisie' if has_progress else 'Aucune saisie'),
        ('quality', 'verified', 'Malfaçons ouvertes', str(defects), 'Ouvertes ou en cours'),
    ]
    for column, (key, icon, label, value, detail) in zip(columns, values):
        with column:
            with st.container(key='dash_kpi_'+key):
                st.markdown(f':material/{icon}: **{label}**')
                st.metric(label, value, label_visibility='collapsed')
                st.caption(detail)
    st.space('small')
    st.subheader('Actions rapides')
    actions=[('daily','Rapport du jour','edit_note','Chantiers','Rapport du jour'),
             ('cost','Dépenses','add_card','Finances','Dépenses'),
             ('quality','Qualité','fact_check','Qualité','Malfaçons'),
             ('analysis','Analyses probabilistes','query_stats','Analyses probabilistes','Analyses probabilistes')]
    for column,(key,label,icon,domain,section) in zip(st.columns(4),actions):
        with column:
            with st.container(key='dash_action_'+key):
                st.button(label,icon=f':material/{icon}:',on_click=dashboard_route,args=(domain,section),width='stretch',key='dash_go_'+key)
    st.space('small')
    left,right=st.columns(2)
    with left:
        st.subheader('Répartition des dépenses')
        totals=db.rows('SELECT categorie,SUM(montant_fcfa) total FROM depenses WHERE chantier_id=? AND supprime=0 GROUP BY categorie',(cid,))
        names={'materiaux':'Matériaux','main_oeuvre':'Main-d’œuvre','materiel':'Matériel','transport':'Transport','sous_traitance':'Sous-traitance','autre':'Autre'}
        if totals and sum(float(row['total']) for row in totals)>0:
            fig=go.Figure(go.Pie(labels=[names.get(row['categorie'],row['categorie']) for row in totals],values=[row['total'] for row in totals],hole=.68,textinfo='percent',textposition='inside',marker=dict(colors=['#3679d8','#26a47d','#e4a331','#cc6080','#6c7f94','#56adca']),hovertemplate='%{label}<br>%{value:,.0f} FCFA<extra></extra>'))
            fig.update_layout(height=320,margin=dict(l=10,r=10,t=15,b=70),paper_bgcolor='rgba(0,0,0,0)',font=dict(color='#35445c'),legend=dict(orientation='h',y=-.12,x=0))
            st.plotly_chart(fig,width='stretch',key='dash_costs')
        else:
            st.info('Aucune dépense enregistrée pour ce chantier.')
    with right:
        st.subheader('Évolution de l’avancement')
        rows=db.rows('SELECT date_saisie,pourcentage FROM avancement WHERE chantier_id=? AND supprime=0 ORDER BY date_saisie,id',(cid,))
        if rows:
            # Use the latest entry of each day, not an average of successive updates.
            daily={row['date_saisie']:float(row['pourcentage']) for row in rows}
            fig=go.Figure(go.Scatter(x=list(daily),y=list(daily.values()),mode='lines+markers',fill='tozeroy',fillcolor='rgba(38,164,125,.12)',line=dict(color='#26a47d',width=3),marker=dict(size=8),hovertemplate='%{x}<br>%{y:.1f} %<extra></extra>'))
            fig=chart_style(fig,'','Date','Avancement (%)',320)
            fig.update_yaxes(range=[0,100]);fig.update_xaxes(type='date')
            st.plotly_chart(fig,width='stretch',key='dash_progress')
        else:
            st.info('Aucun avancement saisi pour ce chantier.')
    st.subheader('Situation du chantier')
    a,b=st.columns(2)
    with a:
        if budget>0:
            st.progress(min(1.,max(0.,spent/budget)),text=f'Budget consommé : {spent/budget:.1%}')
            if remaining<0: st.error(f'Dépassement du budget : {-remaining:,.0f} FCFA')
            else: st.success(f'Budget restant : {remaining:,.0f} FCFA')
        else: st.info('Définissez un budget pour suivre sa consommation.')
    with b:
        st.progress(min(1.,max(0.,progress/100)),text=f'Avancement physique : {progress:.1f} %' if has_progress else 'Avancement non renseigné')
        if defects: st.warning(f'{defects} malfaçon(s) à traiter')
        else: st.success('Aucune malfaçon ouverte enregistrée')
    st.subheader('Dernières dépenses')
    latest=db.rows('SELECT date_depense,libelle,categorie,montant_fcfa FROM depenses WHERE chantier_id=? AND supprime=0 ORDER BY date_depense DESC,id DESC LIMIT 5',(cid,))
    records(latest,'dashboard_latest','Dernières dépenses')
    with st.expander('Alertes du chantier'):
        alerts(db,cid,user)


STATUT_LABELS={'prevu':'Prévu','en_cours':'En cours','suspendu':'Suspendu','termine':'Terminé'}


def local_workspace_user(database):
    """Keep audit ownership without asking the user for personal credentials."""
    identity = '__geniecivil_local_workspace__'
    with database.transaction():
        if database.postgres:
            database.conn.execute('LOCK TABLE utilisateurs IN EXCLUSIVE MODE')
        rows = database.rows('SELECT id,identifiant,nom_complet,role,actif FROM utilisateurs WHERE identifiant=?', (identity,))
        if not rows:
            # This random verifier is not a shared password and is never exposed.
            verifier = hashlib.sha256(secrets.token_bytes(64)).hexdigest()
            database.conn.execute('INSERT INTO utilisateurs(identifiant,nom_complet,mot_de_passe_hash,role) VALUES(?,?,?,?)',
                                  (identity, 'Espace local', verifier, 'admin'))
            rows = database.rows('SELECT id,identifiant,nom_complet,role,actif FROM utilisateurs WHERE identifiant=?', (identity,))
        user = rows[0]
        if not user['actif'] or user['role'] != 'admin':
            raise ValueError('L’identité technique locale est inactive ou incompatible. Vérifiez la base de données utilisée.')
        return {key:user[key] for key in ('id','identifiant','nom_complet','role')}

STYLE = STYLE.replace('</style>', '''
.stApp { background:#eef3f5; }
[data-testid="stSidebar"] { background:#173f3c; border-right:0; }
[data-testid="stSidebar"] h3, [data-testid="stSidebar"] label,
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] { color:#edf7f4 !important; }
[data-testid="stSidebar"] button[kind="secondary"] { background:#244f4b; color:#fff; border-color:#3b6963; text-align:left; }
[data-testid="stSidebar"] button:hover { border-color:#50d6b0; }
[data-testid="stSidebar"] [data-testid="stBadge"] { color:#e9fff6 !important; background:#285b51 !important; }
[data-testid="stSidebar"] [data-testid="stBaseButton-primary"] { background:#147c68 !important; border-color:#50bda3 !important; }
.app-masthead { background:#173f3c; border-bottom:6px solid #24b991; padding:26px 30px; margin:0 0 22px; color:white; position:relative; overflow:hidden; }
.app-masthead h1 { color:white !important; margin:0 !important; padding:0 !important; font-size:2rem !important; line-height:1.25; }
.app-masthead p { color:#d2e9e3; margin:10px 0 0; }
.app-masthead .eyebrow { color:#83e6c8; font-size:12px; font-weight:700; margin:0 0 8px; letter-spacing:0; }
.masthead-colors { display:flex; height:7px; margin-top:22px; width:180px; max-width:100%; }
.masthead-colors span { flex:1; background:#42c9a1; }
.masthead-colors span:nth-child(2) { background:#4285de; }
.masthead-colors span:nth-child(3) { background:#f2b847; }
.masthead-colors span:nth-child(4) { background:#e56687; }
[class*="st-key-dash_kpi_"] { border:0; border-radius:6px; box-shadow:none; }
.st-key-dash_kpi_budget { background:#2564b4; }
.st-key-dash_kpi_spent { background:#a95b17; }
.st-key-dash_kpi_progress { background:#14745c; }
.st-key-dash_kpi_quality { background:#ab3d62; }
[class*="st-key-dash_kpi_"] [data-testid="stMetricValue"],
[class*="st-key-dash_kpi_"] [data-testid="stMetricLabel"],
[class*="st-key-dash_kpi_"] [data-testid="stCaptionContainer"],
[class*="st-key-dash_kpi_"] p { color:white !important; }
[class*="st-key-dash_kpi_"] [data-testid="stCaptionContainer"] { opacity:1 !important; }
[data-testid="stForm"] { background:#f7fbfa; border:1px solid #cadbd7; border-top:4px solid #159a78; border-radius:6px; }
[data-testid="stBaseButton-primary"], [data-testid="stFormSubmitButton"] button { background:#14745c !important; border-color:#14745c !important; color:white !important; }
[data-testid="stBaseButton-primary"]:hover { background:#0f5947 !important; }
[data-testid="stTextInput"] input, [data-testid="stNumberInput"] input, textarea { background:#fff; }
.st-key-dash_action_daily button { background:#14745c; color:white; border-color:#14745c; }
.st-key-dash_action_cost button { background:#a95b17; color:white; border-color:#a95b17; }
.st-key-dash_action_quality button { background:#ab3d62; color:white; border-color:#ab3d62; }
.st-key-dash_action_analysis button { background:#2564b4; color:white; border-color:#2564b4; }
.empty-workspace { border-left:5px solid #159a78; padding:18px 22px; background:#dceee8; margin:16px 0; }
.empty-workspace h3 { color:#173f3c; margin:0 0 6px; font-size:1.25rem; }
.empty-workspace p { color:#31564d; margin:0; }
@media(max-width:640px) {
 .app-masthead { padding:22px 18px; }
 .app-masthead h1 { font-size:1.7rem !important; }
 .app-masthead p { font-size:14px; }
}
</style>''')

# STREAMLIT APPLICATION
import datetime as dt
import io
import sqlite3

import pandas as pd
import streamlit as st

st.set_page_config(page_title='Génie civil pro', page_icon=':material/construction:', layout='wide')
install_layout()
st.html('''<header class="app-masthead">
<p class="eyebrow">PILOTAGE DES TRAVAUX</p>
<h1>Génie Civil Pro</h1>
<p>Chantiers &nbsp; / &nbsp; Budget &nbsp; / &nbsp; Qualité &nbsp; / &nbsp; Probabilités</p>
<div class="masthead-colors" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
</header>''')
try:
    database_url = st.secrets.get('DATABASE_URL', None)
except FileNotFoundError:
    database_url = None
db = Database(url=database_url)
if 'flash' in st.session_state:
    st.success(st.session_state.pop('flash'))


def save(table, values, user):
    try:
        db.insert(table, values, user)
        st.success('Enregistrement effectué.')
    except Exception as exc:
        st.error(str(exc) if isinstance(exc,ValueError) else 'Enregistrement impossible : vérifiez les références et les codes uniques.')


try:
    try:
        user = local_workspace_user(db)
    except ValueError as exc:
        st.error(str(exc))
        st.stop()
    if st.session_state.get('direct_access_revision') != 1:
        for key in list(st.session_state):
            if key.startswith('ana_') or key in ('analysis_scope', 'report'):
                del st.session_state[key]
        st.session_state.domain = 'Synthèse'
        st.session_state.section = 'Synthèse'
        st.session_state.direct_access_revision = 1
    st.session_state.user = user
    editable = True
    db.admin = True
    with st.sidebar:
        st.subheader('Espace chantier')
        st.badge('Accès direct', icon=':material/computer:', color='blue')
    domains = {
        'Synthèse': ['Synthèse'],
        'Chantiers': ['Chantiers', 'Rapport du jour', 'Journalier', 'Avancement', 'Matériel'],
        'Finances': ['Dépenses', 'Devis'],
        'Qualité': ['Malfaçons'],
        'Analyses probabilistes': ['Analyses probabilistes'],
        'Administration': ['Sauvegardes', 'Historique', 'Archives'],
    }
    st.sidebar.button('Tableau de bord',icon=':material/dashboard:',type='primary',width='stretch',on_click=dashboard_route,args=('Synthèse','Synthèse'),key='dashboard_home')
    for nav_domain, nav_icon in [('Chantiers','construction'), ('Finances','payments'), ('Qualité','verified'), ('Analyses probabilistes','query_stats'), ('Administration','settings')]:
        st.sidebar.button(nav_domain, icon=f':material/{nav_icon}:', width='stretch',
                          on_click=dashboard_route, args=(nav_domain,domains[nav_domain][0]), key=f'nav_{nav_icon}')
    domain = st.sidebar.selectbox('Domaine', list(domains), key='domain')
    section = st.sidebar.selectbox('Rubrique', domains[domain], key='section')
    sites = db.sites(user)
    site_map = {row['id']: row for row in sites}
    cid = st.selectbox('Chantier', list(site_map), format_func=lambda key: f"{site_map[key]['code']} - {site_map[key]['nom']}") if sites else None

    st.divider()
    st.subheader('Tableau de bord' if section == 'Synthèse' else section)
    if cid:
        db.access(cid,user)
    if section == 'Historique':
        history(db,cid,user)
    elif section == 'Archives':
        archived=db.sites(user,archived=True)
        records(archived,'archived_sites','Chantiers archivés')
        if archived:
            rid=st.selectbox('Chantier à restaurer',[r['id'] for r in archived])
            if st.button('Restaurer le chantier',icon=':material/restore:'):
                action(lambda:db.archive('chantiers',rid,user,restore=True))
        if cid:
            table=st.selectbox('Archives du chantier',['depenses','avancement','journalier','malfacons','materiel','devis'])
            archived_rows=db.rows(f'SELECT * FROM {table} WHERE chantier_id=? AND supprime=1',(cid,))
            records(archived_rows,'archives_records','Archives')
            if archived_rows:
                rid=st.selectbox('Enregistrement à restaurer',[r['id'] for r in archived_rows])
                if st.button('Restaurer l’enregistrement',icon=':material/restore:'):
                    action(lambda:db.archive(table,rid,user,restore=True))
    elif section == 'Chantiers':
        if editable:
            with st.form('site'):
                code = st.text_input('Code')
                name = st.text_input('Nom du chantier')
                client = st.text_input('Client')
                loc = st.text_input('Localisation')
                budget = st.number_input('Budget (FCFA)', min_value=0.0, step=1000.0)
                debut = st.date_input('Date de début')
                fin = st.date_input('Date de fin prévue')
                if st.form_submit_button('Créer le chantier', icon=':material/add:', width='stretch'):
                    save('chantiers', dict(code=code.strip(), nom=name.strip(), client=client, localisation=loc, budget_fcfa=budget, date_debut=debut.isoformat(), date_fin_prevue=fin.isoformat()), user)
        site_rows=db.sites(user)
        records(filter_rows(site_rows,'sites'), 'sites', 'Chantiers')
        manage(db,'chantiers',site_rows,user)
    elif section == 'Sauvegardes':
        if db.admin and not db.postgres:
            st.download_button('Télécharger la sauvegarde SQLite', db.backup(), file_name=f'genie-civil-{dt.date.today()}.db', mime='application/octet-stream', icon=':material/download:', width='stretch')
            st.caption('La sauvegarde inclut les comptes utilisateurs. Conservez-la dans un emplacement privé.')
        if cid:
            if st.button('Préparer le rapport PDF',icon=':material/picture_as_pdf:',width='stretch'):
                st.session_state.report = (cid,report_with_analysis(db,cid,user))
            if st.session_state.get('report',(None,))[0]==cid:
                st.download_button('Télécharger le rapport PDF',st.session_state.report[1],file_name=f'chantier-{cid}.pdf',mime='application/pdf',width='stretch')
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                for table in ('journalier', 'malfacons', 'depenses', 'avancement', 'materiel', 'devis'):
                    pd.DataFrame(db.rows(f'SELECT * FROM {table} WHERE chantier_id=? AND supprime=0', (cid,))).to_excel(writer, sheet_name=table, index=False)
            st.download_button('Exporter le chantier en Excel', output.getvalue(), file_name=f'chantier-{cid}.xlsx', icon=':material/download:', width='stretch')
        st.caption('Pour Google Drive, déposez le fichier téléchargé dans votre dossier synchronisé et utilisez le véritable lien de partage fourni par Drive.')
    elif section == 'Analyses probabilistes' and cid:
        analysis_workspace(db,cid,user)
    elif not cid:
        for column, tone, label, value in zip(st.columns(4), ['budget','spent','progress','quality'],
                ['Chantiers actifs','Dépenses enregistrées','Avancement','Malfaçons ouvertes'], ['0','0 FCFA','—','0']):
            with column, st.container(key=f'dash_kpi_{tone}'):
                st.metric(label, value)
                st.caption('Aucun chantier sélectionné')
        st.html('<section class="empty-workspace"><h3>Votre espace chantier est prêt</h3><p>Aucun chantier enregistré pour le moment.</p></section>')
        if editable:
            st.button('Créer mon premier chantier',icon=':material/add:',type='primary',on_click=dashboard_route,args=('Chantiers','Chantiers'))
    elif section == 'Synthèse':
        dashboard(db,cid,user)
    elif section == 'Rapport du jour':
        if not editable:
            st.info('Votre compte permet la consultation uniquement.')
        else:
            with st.form('quick_report'):
                date=st.date_input('Date du rapport')
                meteo=st.text_input('Météo')
                effectif=st.number_input('Effectif',min_value=0)
                travaux=st.text_area('Travaux réalisés')
                incidents=st.text_area('Incidents')
                photo=st.file_uploader('Photo du jour',type=['jpg','jpeg','png'],max_upload_size=5)
                if st.form_submit_button('Enregistrer le rapport du jour',icon=':material/save:',width='stretch'):
                    def quick_save():
                        # A failed photo must not leave a half-saved journal entry.
                        with db.transaction():
                            rid=db.insert('journalier',dict(chantier_id=cid,date_jour=date.isoformat(),meteo=meteo,effectif=effectif,travaux_realises=travaux,incidents=incidents),user)
                            if photo: db.photo('journalier',rid,'Journalier',photo.getvalue(),user)
                    action(quick_save)
    else:
        specs = {
            'Journalier': ('journalier', [('date_jour','Date','date'), ('meteo','Météo','text'), ('effectif','Effectif','int'), ('travaux_realises','Travaux réalisés','area'), ('incidents','Incidents','area')]),
            'Malfaçons': ('malfacons', [('element','Élément','text'), ('type_defaut','Type de défaut','text'), ('criticite','Criticité',['Faible','Moyenne','Élevée','Critique']), ('description','Description','area'), ('action_corrective','Action corrective','area')]),
            'Dépenses': ('depenses', [('categorie','Catégorie',['materiaux','main_oeuvre','materiel','sous_traitance','transport','autre']), ('libelle','Libellé','text'), ('montant_fcfa','Montant (FCFA)','number'), ('date_depense','Date','date'), ('reference_piece','Référence de pièce','text')]),
            'Avancement': ('avancement', [('pourcentage','Avancement (%)','percent'), ('description','Description','area'), ('date_saisie','Date','date')]),
            'Matériel': ('materiel', [('designation','Désignation','text'), ('quantite','Quantité','number'), ('unite','Unité','text'), ('date_reception','Date de réception','date')]),
            'Devis': ('devis', [('numero','Numéro','text'), ('objet','Objet','text'), ('tva_pct','TVA (%)','percent')]),
        }
        table, fields = specs[section]
        if editable:
            with st.form('record'):
                values = {'chantier_id': cid}
                for key, label, kind in fields:
                    if isinstance(kind, list):
                        values[key] = st.selectbox(label, kind)
                    elif kind == 'date':
                        values[key] = st.date_input(label).isoformat()
                    elif kind in ('int', 'number', 'percent'):
                        values[key] = st.number_input(label, min_value=0 if kind == 'int' else 0.0, max_value=100.0 if kind == 'percent' else None, value=19.25 if key == 'tva_pct' else (0 if kind == 'int' else 0.0))
                    elif kind == 'area':
                        values[key] = st.text_area(label)
                    else:
                        values[key] = st.text_input(label)
                if table == 'malfacons':
                    values['date_signalement'] = dt.date.today().isoformat()
                if st.form_submit_button('Enregistrer', icon=':material/save:', width='stretch'):
                    save(table, values, user)
        rows = db.rows(f'SELECT * FROM {table} WHERE chantier_id=? AND supprime=0 ORDER BY id DESC', (cid,))
        records(filter_rows(rows,table), table, f'Liste : {section}')
        manage(db,table,rows,user)
        if table in ('malfacons','journalier'):
            photos(db,table,rows,cid,user)
        if table == 'malfacons' and rows and editable:
            with st.form('resolve'):
                rid = st.selectbox('Malfaçon', [row['id'] for row in rows])
                status = st.selectbox('Résolution', ['Ouvert', 'En cours', 'Résolu'])
                if st.form_submit_button('Modifier le statut', icon=':material/check:', width='stretch'):
                    db.update('malfacons',rid,{'statut_resolution':status},user)
                    st.rerun()
        if table == 'devis' and rows:
            did = st.selectbox('Devis', [row['id'] for row in rows], format_func=lambda key: next(row['numero'] for row in rows if row['id'] == key))
            if editable:
                with st.form('quote_line'):
                    des = st.text_input('Désignation de la ligne')
                    unit = st.text_input('Unité de la ligne', value='u')
                    qty = st.number_input('Quantité de la ligne', min_value=0.0)
                    price = st.number_input('Prix unitaire (FCFA)', min_value=0.0)
                    if st.form_submit_button('Ajouter la ligne', icon=':material/add:', width='stretch'):
                        save('lignes_devis', dict(devis_id=did, designation=des, unite=unit, quantite=qty, prix_unitaire_fcfa=price), user)
            lines = db.rows('SELECT * FROM lignes_devis WHERE devis_id=? AND supprime=0', (did,))
            records(lines, 'quote_lines', 'Lignes du devis')
            manage(db,'lignes_devis',lines,user)
            ht = sum(row['quantite'] * row['prix_unitaire_fcfa'] for row in lines)
            vat = next(row['tva_pct'] for row in rows if row['id'] == did)
            st.metric('Total TTC (FCFA)', f'{ht * (1 + vat / 100):,.0f}')
finally:
    db.conn.close()
