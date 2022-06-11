# realip-ingress-testapp

an application to test x-real-ip in kubernetes ingress for external loadbalancer and also a simple k8s base model.

# docker build and push to docker-hub

```
docker build -t joaoreis/realip-ingress-testapp ./code
docker push joaoreis/realip-ingress-testapp
```
# kubectl deploy 

```
kubectl --kubeconfig ~/.kube/config_intesys_dev_sandbox1 create namespace development --dry-run=client -o yaml | kubectl apply -f -
kubectl --kubeconfig ~/.kube/config_intesys_dev_sandbox1 -n development delete -f ./kube-deploy.yml
kubectl --kubeconfig ~/.kube/config_intesys_dev_sandbox1 -n development apply -f ./kube-deploy.yml 
```
