import time
import subprocess

def slikube_timer():
    all_start = time.time()
    for i in range(5):
        start_time = time.time()
        #subprocess.run(["docker", "run", "--rm", "-v", "/Users/shamim/WR_23/helm_manifests/all_helm_charts:/iac", "--name", "slikube", "slikube", "/iac" ])
        #Baseline
        subprocess.run(["docker", "run", "--rm", "-v", "/Users/shamim/WR_23/helm_manifests/all_helm_charts:/iac", "--name", "akondrahman/sli-kube", "sli-kube:latest", "/iac" ])
        end_time = time.time()
        print("SLIKUBE RUN #",i+1, "=", end_time - start_time)
    all_end = time.time()
    print("KubeScape Average: ", (all_end - all_start)/5)

def kubescape_timer():
    all_start = time.time()
    for i in range(5):
        start_time = time.time()
        subprocess.run(["kubescape", "scan", "/Users/shamim/WR_23/helm_manifests/all_helm_charts", "--format", "sarif", "--output", "kubescape-result.sarif"])
        end_time = time.time()
        print("KUBESCAPE RUN #",i, "=",end_time - start_time)
    all_end = time.time()
    print("KubeScape Average: ", (all_end - all_start)/5)
    


def checkov_timer():
    all_start = time.time()
    for i in range(5):
        start_time  = time.time()
        subprocess.run(["checkov", "-d", "/Users/shamim/WR_23/helm_manifests/all_helm_charts", "--framework", "kubernetes", "-o", "sarif"])
        end_time = time.time()
        print("CHECKOV RUN #",i+1, "=", end_time - start_time)
    all_end = time.time()
    print("Checkov Average: ", (all_end - all_start)/5)



def kubelinter_timer():
    all_start = time.time()
    for i in range(5):
        start_time  = time.time()
        subprocess.run(["kube-linter", "lint", "/Users/shamim/WR_23/helm_manifests/all_helm_charts", "--config", "/Users/shamim/WR_23/kubelinter-config.yaml", "--format=sarif"])
        end_time = time.time()
        print("KUBELINTER RUN #",i+1, "=", end_time - start_time)
    all_end = time.time()
    print("Kubelinter Average: ", (all_end - all_start)/5)


def trivy_timer():
    all_start = time.time()
    for i in range(5):
        start_time  = time.time()
        subprocess.run(["trivy", "fs", "--scanners", "config", "/Users/shamim/WR_23/helm_manifests/all_helm_charts", "--format", "sarif", "-o", "trivy-output.sarif"])
        end_time = time.time()
        print("TRIVY RUN #",i+1, "=", end_time - start_time)
    all_end = time.time()
    print("Trivy Average: ", (all_end - all_start)/5)



if __name__ == "__main__":
    # kubescape_timer()   
    # checkov_timer()
    # kubelinter_timer()
    # trivy_timer()
    slikube_timer()






##### SLIKUBE updated ##### 
# docker run --rm -v /Users/shamim/WR_23/helm_manifests/all_helm_charts:/iac --name slikube slikube /iac
# 1 1861.0438561439514
# SLIKUBE RUN # 1 = 2566.535991191864
# SLIKUBE RUN # 2 = 40011.89341688156
# SLIKUBE RUN # 3 = 2384.8920571804047
# SLIKUBE RUN # 4 = 1116.97163271904
# SLIKUBE RUN # 5 = 5027.179378032684
# 

##### SLIKUBE baseline #####


##### KUBE-LINTER #####
# kube-linter lint /Users/shamim/WR_23/helm_manifests/all_helm_charts --config kubelinter-config.yaml --format=sarif
# Kubelinter Average:  0.21708302497863768

##### KUBESCAPE #####
# kubescape scan /Users/shamim/WR_23/helm_manifests/all_helm_charts --format sarif --output kubescape-result.sarif
# KubeScape Average:  7.85125036239624

##### CHECKOV #####
# checkov -d /Users/shamim/WR_23/helm_manifests/all_helm_charts --framework kubernetes -o sarif
# Checkov Average:  3.843128204345703

##### TRIVY #####
# trivy fs --scanners config /Users/shamim/WR_23/helm_manifests/all_helm_charts --format sarif -o trivy-output.sarif 
# TRIVY RUN # 1 = 32.55004167556763
# TRIVY RUN # 2 = 35.32548475265503
# TRIVY RUN # 3 = 32.57321095466614
# TRIVY RUN # 4 = 32.355316162109375
# TRIVY RUN # 5 = 33.15369200706482
# Trivy Average:  33.19167037010193

