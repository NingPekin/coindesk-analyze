import json
import requests
import pandas as pd
# get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt


class BitCoin:

    def get_data_period(start,end):
        response = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=%s&end=%s'%(start,end));
        # print(response);
        json_data = json.loads(response.text);
        # print (json_data);
        json_bpi=json_data['bpi'];
        # print (json_bpi)
        arr_bpi_data=[];
        for value in json_bpi.items():
            # print (value[1]);
            arr_bpi_data.append(value[1]);
        # print(arr_bpi_data);
        min_bpi_data=min(arr_bpi_data,key=float);
        print(min_bpi_data);
        max_bpi_data=max(arr_bpi_data,key=float);
        print(max_bpi_data);
        # data_line=pd.Series(bpi);
        # print(data_line);
        # plt.figure(figsize=(15,10));
        # data_line.plot.line();
        # plt.xlabel('Dates',fontsize=20, fontweight='bold');
        # plt.ylabel('Prices',fontsize=20, fontweight='bold');

    def get_data_30days():
        response = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json');
        # print(response);
        json_data = json.loads(response.text);
        # print (json_data);
        json_bpi=json_data['bpi'];
        # print (json_bpi)
        arr_bpi_data=[];
        for value in json_bpi.items():
            # print (value[1]);
            arr_bpi_data.append(value[1]);
        # print(arr_bpi_data);
        min_bpi_data=min(arr_bpi_data,key=float);
        print(min_bpi_data);
        max_bpi_data=max(arr_bpi_data,key=float);
        print(max_bpi_data);

    # get_data_period("2018-02-01","2018-02-15");
    get_data_30days();

