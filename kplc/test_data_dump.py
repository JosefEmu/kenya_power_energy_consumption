import Kenya_Power_Energy_Usage as kplc

august= EnergyUsage(4.6, "20180801")
august.add_tokens(4.6,100)
august.add_tokens(4.6,100)
august.add_tokens(4.6,100)
august.add_tokens(13.6,300)
august.add_tokens(2.25,50)
august.add_tokens(4.51,100)
august.add_tokens(4.51,100)
august.add_tokens(2.25,50)
august.add_tokens(4.51,100)
august.add_tokens(4.51,100)
august.add_tokens(2.48,55)
august.add_tokens(2.25,50)
august.add_tokens(0.99,22)
august.add_tokens(3.52,78)
august.add_tokens(4.51,100)
august.monthly_usage("20180831",0)

september= EnergyUsage(0.0, "20180901")
september.add_tokens(4.6, 100)
september.add_tokens(4.6, 100)
september.add_tokens(23, 500)
september.add_tokens(9.2, 200)
september.monthly_usage("20180930",0.0)

october= EnergyUsage(0.0, "20181002")
october.add_tokens(9.2, 200)
october.add_tokens(13.8, 300)
october.add_tokens(8.6, 188)
october.add_tokens(13.8, 300)
october.add_tokens(4.6, 100)
october.monthly_usage("20181031",4.66)

november= EnergyUsage(0.0, "20181101")
november.add_tokens(4.6, 100)
november.add_tokens(6.7, 100)
november.add_tokens(6.7, 100)
november.add_tokens(6.6, 100)
november.add_tokens(6.6, 100)
november.add_tokens(13.2, 200)
november.add_tokens(6.6, 100)
november.monthly_usage("20181130",0.0)

december= EnergyUsage(0.0, "20181201")
december.add_tokens(6.6, 100) 
december.add_tokens(6.6, 100)
december.add_tokens(6.6, 100)
december.add_tokens(1.5, 22)
december.monthly_usage("20181216",1.62)

