from init import app
import init
import api,config,model

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5050)