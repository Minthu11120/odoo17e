FROM odoo:17.0

USER root

# တကယ်လို့ လိုအပ်ရင် custom addons လမ်းကြောင်းကို ဒီမှာ ညွှန်းနိုင်ပါတယ်
# COPY ./odoo-17.0+e.20250808/addons /mnt/extra-addons

USER odoo
