__author__ = 'Alessio'

from project import model_
from project import db, bycrypt_on_pass_user

#primo = model_.profile_type_(name="Admin")
#print primo.name
#terzo = model_.profile_type_(name="User",permission=1)
#ad=model_.user_("administrator1",bycrypt_on_pass_user.generate_password_hash('binocchio19771'),"admin112111@admin.it","alessio","bino",primo.name)
#db.session.add(ad)
#db.session.commit()
my_q = db.session.query(model_.profile_type_.name).all()
print my_q