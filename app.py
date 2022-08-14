{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d321505",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask,render_template,request"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a6948cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ecc19c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "303b9c1a",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'app' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [3]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;129m@app\u001b[39m\u001b[38;5;241m.\u001b[39mroute(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m/\u001b[39m\u001b[38;5;124m\"\u001b[39m,methods \u001b[38;5;241m=\u001b[39m [\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mGET\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPOST\u001b[39m\u001b[38;5;124m\"\u001b[39m])\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mindex\u001b[39m():\n\u001b[1;32m      3\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m request\u001b[38;5;241m.\u001b[39mmethod \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPOST\u001b[39m\u001b[38;5;124m\"\u001b[39m:    \n\u001b[1;32m      4\u001b[0m         rates \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mfloat\u001b[39m(request\u001b[38;5;241m.\u001b[39mform\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mrates\u001b[39m\u001b[38;5;124m\"\u001b[39m))\n",
      "\u001b[0;31mNameError\u001b[0m: name 'app' is not defined"
     ]
    }
   ],
   "source": [
    "@app.route(\"/\",methods = [\"GET\", \"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":    \n",
    "        rates = float(request.form.get(\"rates\"))\n",
    "        print (rates)\n",
    "        model1= joblib.load(\"regression_DBS\")\n",
    "        pred1 = model1.predict([[rates]])\n",
    "        model2 = joblib.load(\"tree_DBS\")\n",
    "        pred2 = model2.predict([[rates]])\n",
    "        return(render_template(\"index.html\", result = pred1, result2= pred2))\n",
    "    else:\n",
    "        return(render_template(\"index.html\", result1= \"waiting\", result2=\"waiting\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "06ebbb21",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'app' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [2]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[0;32m----> 2\u001b[0m     \u001b[43mapp\u001b[49m\u001b[38;5;241m.\u001b[39mrun()\n",
      "\u001b[0;31mNameError\u001b[0m: name 'app' is not defined"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27eff8df",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
