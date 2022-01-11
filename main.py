# python speed tester 
# pip install speetest-cli
import speedtest
st = speedtest.Speedtest()
option = int(input(''' what speed to you want to test
                   1) Download speed 
                   2) Upload speed 
                   3) Ping
                   Your choice:
                   '''))

if option == 1:
    print(st.download())
elif option == 2:
    print(st.upload())
elif option == 3:
    servernames = []    
# Author: Jayson
# twitter: jay_b_jayson
    st.get_servers(servernames)
    print(st.results.ping)
else:
    print("please enter the correct choice!")
    