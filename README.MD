This is a starter template for combining vue 3 and flask.  
I noticed every single online article involved JWT and decided to implement session id.  
Its not perfect or done but a good template starter.  


# Frontend 
Vue 3 and Quasar
<code>
npm install -g @quasar/cli
npm install --save vuex-persistedstate
quasar create frontend
</code>

# Backend
Python flask

<code>
sudo apt-get install virtualenv
virtualenv venv -p python
source venv/bin/activate
pip3 install -r requirements.txt

python3 run.py
</code>