FROM odoo:17.0

USER root

# ၁။ Odoo Enterprise Folder ကို ကူးထည့်ခြင်း
COPY ./odoo-17.0+e.20250808 /workspaces/odoo

# ၂။ Enterprise Addons လမ်းကြောင်းကို Config ထဲ ထည့်ခြင်း
RUN sed -i '/addons_path/d' /etc/odoo/odoo.conf && \
    echo "addons_path = /workspaces/odoo/addons,/usr/lib/python3/dist-packages/odoo/addons" >> /etc/odoo/odoo.conf

# ၃။ Hugging Face ရဲ့ ပုံမှန် Port 7860 ကို ပြောင်းလဲသတ်မှတ်ခြင်း
# (Hugging Face က Port 7860 ကလွဲရင် ကျန်တာကို ပေးမပွင့်လို့ ဖြစ်ပါတယ်)
EXPOSE 7860
ENV PORT=7860

# ၄။ Odoo ကို Port 7860 နဲ့ ပွင့်လာအောင် အမိန့်ပေးခြင်း
CMD ["odoo", "--http-port=7860"]

USER odoo
