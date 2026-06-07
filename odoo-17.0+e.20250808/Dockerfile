FROM odoo:17.0

USER root

# ၁။ သင့် GitHub ထဲက Enterprise Folder ကို ကူးထည့်ခြင်း
COPY ./odoo-17.0+e.20250808 /workspaces/odoo

# ၂။ config ဖိုင်ဟောင်းထဲမှာ addons_path ရှိပြီးသားစာသားကို ဖျက်ပြီး ကျွန်တော်တို့ လမ်းကြောင်းအသစ်နဲ့ အစားထိုးခြင်း
RUN sed -i '/addons_path/d' /etc/odoo/odoo.conf && \
    echo "addons_path = /workspaces/odoo/addons,/usr/lib/python3/dist-packages/odoo/addons" >> /etc/odoo/odoo.conf

USER odoo
