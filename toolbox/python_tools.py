
# Upper
a="sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule"
b=a.upper()

# Replace
c=b.replace(".","_") #replace the . separator with _