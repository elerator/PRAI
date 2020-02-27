# prai_information_desk
[![build status](https://gitlab.roqs.basf.net/GersteM5/prai_information_desk/badges/master/build.svg)](https://gitlab.roqs.basf.net/GersteM5/prai_information_desk/pipelines?scope=branches) 

## Greetings from happypotter

Thanks for using h __app__ y potter to create this Python RestPlus API. :zap:

For pod information and logs, try Kubecuddle:

- [Kubecuddle Development](https://app-dev.roqs.basf.net/kubecuddle/v2/pod.html?deployment=prai-information-desk&namespace=prai-information-desk-dev)
- [Kubecuddle QA](https://app-qa.roqs.basf.net/kubecuddle/v2/pod.html?deployment=prai-information-desk&namespace=prai-information-desk-qual)
- [Kubecuddle Production](https://app.roqs.basf.net/kubecuddle/v2/pod.html?deployment=prai-information-desk&namespace=prai-information-desk-prod)

For additional logs, try Kibana:

- [Kibana Development](https://app-dev.roqs.basf.net/kibana/app/kibana#/discover?_g=()&_a=(columns:!(message),index:'531e0890-ce55-11e9-b491-8b6feaa9763f',interval:auto,query:(language:lucene,query:'docker.container.image:prai_information_desk'),sort:!('@timestamp',desc)))
- [Kibana QA](https://app-qa.roqs.basf.net/kibana/app/kibana#/discover?_g=()&_a=(columns:!(message),index:'531e0890-ce55-11e9-b491-8b6feaa9763f',interval:auto,query:(language:lucene,query:'docker.container.image:prai_information_desk'),sort:!('@timestamp',desc)))
- [Kibana Production](https://app.roqs.basf.net/kibana/app/kibana#/discover?_g=()&_a=(columns:!(message),index:'531e0890-ce55-11e9-b491-8b6feaa9763f',interval:auto,query:(language:lucene,query:'docker.container.image:prai_information_desk'),sort:!('@timestamp',desc)))

### Your current setup

* __Docker__: We already containerized your python API in a slim and fast manner. In case you require additional packages, please install them through the [Dockerfile](Dockerfile#L3). The your API will be ready to be deployed anywhere.
* __CI/CD__: Remeber the days you had to copy over files to some server to make your API available to everyone? Those days are over! We already made sure your API gets automatically build and deployed the moment you make a change! Take a look at your brand new API in the _App Store_ [here](https://app.roqs.basf.net/prai_information_desk/).

### Still looking for a development environment?

If you like Jupyter Notebooks you should have a look at our [JupyterHub](http://jupyterhub.roqs.basf.net). You are welcome!

## Kubernetes network policies

Your application has been deployed by Happy Potter with a Kubernetes [ingress
network
policy](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
in place. This policy will shield your application from direct access by other
AppStore applications. Access to your application is required to pass through
the API gateway (https://apps.roqs.basf.net).

The resource declaration can be found in the networkpolicy.yaml file included in
this project by Happy Potter. This file is added for reference only: the
developer does not have the access rights to modify or delete the policy.

## Don't forget to update this README.md!

It's nice when you are greeted with a nice readme file right? Therefore don't forget to update this README.md file so that people visiting your App project can understand what it's all about!