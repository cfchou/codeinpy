__author__ = 'chifeng'

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import sessionmaker
import re

Base = declarative_base()

class Packageinfo(Base):
    __tablename__ = 'ota_packageinfo'

    pkgOid = Column(Integer, primary_key=True, autoincrement=True,
                    nullable=False)
    operOid = Column(Integer, index=True)
    pkgUid = Column(String(200), unique=True)
    prodName = Column(String(200), index=True)
    pkgType = Column(Integer)
    pkgFileExists = Column(TINYINT(1))
    pkgFileName = Column(String(200))
    pkgFileMd5Value = Column(String(32))
    newVersion = Column(String(200))
    oldVersion = Column(String(200))
    pkgUrl = Column(String(200))
    status = Column(Integer)
    pkgRange = Column(Integer)
    country = Column(String(200))
    forUpdate = Column(TINYINT(1))
    queryIntvl = Column(Integer)
    createTime = Column(TIMESTAMP)
    updateTime = Column(TIMESTAMP)
    groupList = Column(String(255))
    # TODO: add FOREIGN KEY operOid
    def __repr__(self):
        return "<PackageInfo(pkgOid='%i', pkgUrl='%s')>" % (self.pkgOid, self.pkgUrl)


# engine = create_engine("mysql://tasadm:tasadm@127.0.0.1:3306/tctas", echo=True)
engine = create_engine("mysql://gmdbadm:gmdbadm123@gm-tasadm.ceodkjk5xdfw.ap-southeast-1.rds.amazonaws.com:3306/tctas", echo=True)
Session = sessionmaker(bind=engine)
sess = Session()

def createTable():
    Base.metadata.create_all (engine)
    Base.metadata.drop_all (engine)

def showRows(res):
    print("-------------------")
    for e in res:
        print("==>> %s" % e)

def insertSome():
    pkg1 = Packageinfo()
    pkg1.pkgUrl = 'https://54.186.221.224:6507/otaiweb/api/download/' \
        'Nexus7II_N7.userdebug_Daily.userdebug_Daily_2014061'
    pkg2 = Packageinfo()
    pkg2.pkgUrl = 'https://54.186.221.162:6507/otaiweb/api/download/' \
                  'Nexus7II_N7.FULL.userdebug_Daily_201406151945_123'
    sess.add_all([pkg1, pkg2])
    sess.commit()


def to162():
    res = sess.query(Packageinfo).order_by(Packageinfo.pkgOid).\
	filter(Packageinfo.pkgUrl.like('%54.186.221.222%'))[:10]
    regex = re.compile('^(?P<proto>(https|http)://)54\.186\.221\.222(?P<path>.+)')
    for e in res:
        oldUrl = e.pkgUrl
        r = regex.search(oldUrl)
        dict = r.groupdict()
        e.pkgUrl = "%s54.179.178.162%s" % (dict.get('proto'), dict.get('path'))
        print("%i,\t\t\t%s\n\t\t\t%s" % (e.pkgOid, oldUrl, e.pkgUrl))
    sess.commit()


def showOld():
    res = sess.query(Packageinfo).order_by(Packageinfo.pkgOid).\
	filter(Packageinfo.pkgUrl.like('%54.186.221.222%'))
    showRows(res)

#showOld()
#insertSome()
to162()


