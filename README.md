# Prai Information Desk
## A project management tool to support agile development and research in production AI
- **Add your project**: Use the group database, document your work and get inspired by previous projects. Search in the database, get to know project partners and enable your collegues to profit from your expertise.
- **Watch your progress**: Keep track of the progress of your projects using the Kanban board and share with your collegues what you've been working on lately.
- **Manage your Workload**: Schedule your capacities according to your work-time-model, oversee how much time you spend on each project and plan your workload in advance.

## Features
Using PrAI is quick & simple: Minimize the administrative overhead of documenting projects and workload to the necessary minimum!
- Centralized information storage in a database
- Web user interface available via the SECRET_COMPANY_NAME App store
- Different views for creation, overview of work-time-models and capacities, project details (…)
- Multiple export options for different bundles of data in form of Excel sheets (.xlsx) and SQLite
- Based on the well established Django-Framework for serverside webdevelopment using Python

## Check it out
- [Development version](https://app-dev.roqs.SECRET_COMPANY_NAME.net/prai_information_desk/)

Kubecuddle:

- [Kubecuddle Development](https://app-dev.roqs.SECRET_COMPANY_NAME.net/kubecuddle/v2/pod.html?deployment=prai-information-desk&namespace=prai-information-desk-dev)
- [Kubecuddle QA](https://app-qa.roqs.SECRET_COMPANY_NAME.net/kubecuddle/v2/pod.html?deployment=prai-information-desk&namespace=prai-information-desk-qual)
- [Kubecuddle Production](https://app.roqs.SECRET_COMPANY_NAME.net/kubecuddle/v2/pod.html?deployment=prai-information-desk&namespace=prai-information-desk-prod)

For additional logs, try Kibana:

- [Kibana Development](https://app-dev.roqs.SECRET_COMPANY_NAME.net/kibana/app/kibana#/discover?_g=()&_a=(columns:!(message),index:'531e0890-ce55-11e9-b491-8b6feaa9763f',interval:auto,query:(language:lucene,query:'docker.container.image:prai_information_desk'),sort:!('@timestamp',desc)))
- [Kibana QA](https://app-qa.roqs.SECRET_COMPANY_NAME.net/kibana/app/kibana#/discover?_g=()&_a=(columns:!(message),index:'531e0890-ce55-11e9-b491-8b6feaa9763f',interval:auto,query:(language:lucene,query:'docker.container.image:prai_information_desk'),sort:!('@timestamp',desc)))
- [Kibana Production](https://app.roqs.SECRET_COMPANY_NAME.net/kibana/app/kibana#/discover?_g=()&_a=(columns:!(message),index:'531e0890-ce55-11e9-b491-8b6feaa9763f',interval:auto,query:(language:lucene,query:'docker.container.image:prai_information_desk'),sort:!('@timestamp',desc)))

## Setup & Local testing
For local testing adjust the settings in ./app/lightweight_research_tool/settings.py i.e. set FORCE_SCRIPT_NAME to an empty string.

If you do not want to use Docker you can start the app locally using "python ./app/manage.py runserver" given django and the other requirements (see requirements.txt) are met and the respective packages installed.

To bypass the SECRET_COMPANY_NAME federation login for local testing edit ./app/landing_page/views.py. Respective comments are left in the code.

Use the export feature to download and replace the database (./database/db.sqlite3) if you desire to make local changes. You can overwrite the existing database in the persistant volume by editing startup.sh (see comments).
