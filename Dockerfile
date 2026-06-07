FROM odoo:17.0

USER root

# ၁။ သင့် GitHub ထဲက Enterprise Folder ကို Docker Image ထဲ ကူးထည့်ခြင်း
COPY ./odoo-17.0+e.20250808 /workspaces/odoo

# ၂။ ပုံမှန် Community လမ်းကြောင်းအစား သင့်ရဲ့ Enterprise Code လမ်းကြောင်းကိုပါ သုံးဖို့ ညွှန်ကြားခြင်း
ENV ODOO_RC=/etc/odoo/odoo.conf
RUN echo "addons_path = /workspaces/odoo/addons,/usr/lib/python3/dist-packages/odoo/addons" >> /etc/odoo/odoo.conf

USER odoo
