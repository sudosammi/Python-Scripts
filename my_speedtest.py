import  speedtest

print("Wait..., Speed Testing")

st = speedtest.Speedtest()


download_speed = st.download() / 10**6

upload_speed = st.upload() / 10**6

ping = st.results.ping 



print("-" * 30)

print(f"🔽 Download Speed : {download_speed:.2f} Mbps")
print(f"🔼 Upload Speed   : {upload_speed:.2f} Mbps")
print(f"📶 Ping / Latency : {ping} ms")

print("-" * 30)
