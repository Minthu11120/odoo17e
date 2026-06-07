FROM odoo:17.0

USER root

# GitHub ထဲက Enterprise Code တွေကို Odoo ရဲ့ Addons လမ်းကြောင်းထဲ ကူးထည့်တာဖြစ်ပါတယ်
COPY ./odoo-17.0+e.20250808 /mnt/enterprise-addons

# Odoo ကို Enterprise Addons လမ်းကြောင်း သိအောင် ညွှန်ပေးခြင်း
ENV ODOO_RC=/etc/odoo/odoo.conf
RUN echo "addons_path = /mnt/enterprise-addons,/usr/lib/python3/dist-packages/odoo/addons" >> /etc/odoo/odoo.conf

USER odoo
