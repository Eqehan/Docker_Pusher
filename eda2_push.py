import os

path = "C:\images1.txt"
url = "default-route-openshift-image-registry.apps.openshiftcluster.westeurope.aroapp.io/eda2/"

os.system('docker login -u egehan.sayan@ericsson.com -p <sha256token> https://default-route-openshift-image-registry.apps.<clustername>.<basedomain>/eda2/')
with open(path, mode='r') as file:
    for line in file:
        #print line
        lineParam = line.split('/')
        size = len(lineParam)-1
        secondParam = lineParam[size].strip()
        dockerCommand = "docker tag" + line.strip() + "" +url +secondParam
        #print docker command
        pushCommand = "docker push"+ url + secondParam
        #print(secondParam)
        #os.system(dockerCommand)
        os.system(pushCommand)

 
