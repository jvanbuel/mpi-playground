
if ! command -v git &> /dev/null
then
    echo "git could not be found"
    exit
fi

if ! command -v kubectl &> /dev/null
then
    echo "git could not be found"
    exit
fi

git clone https://github.com/kubeflow/mpi-operator
cd mpi-operator
kubectl apply -f deploy/v2beta1/mpi-operator.yaml
