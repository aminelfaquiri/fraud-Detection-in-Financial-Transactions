# Détection de Fraude dans les Transactions Financières
![image](https://github.com/aminelfaquiri/fraud-Detection-in-Financial-Transactions/assets/81482544/01e1cc28-e3cc-4836-a748-7e6061708159)

## Introduction

La société "FinTech Innovations" est actuellement confrontée à un défi croissant lié aux transactions frauduleuses, mettant en péril la confiance de nos clients et entraînant des pertes financières importantes. Pour relever ce défi, notre initiative vise à mettre en place un système de détection de fraude basé sur l'analyse de données transactionnelles, de données clients et d'informations externes. L'objectif principal est de détecter en temps réel les activités suspectes tout en minimisant les fausses alertes.

## Objectif du Projet

En tant que développeur Data, l'objectif global demeure la création d'une API nommée `trans_api.py` et la mise en œuvre d'un système de détection de fraude capable d'identifier rapidement les activités suspectes tout en réduisant au maximum les alertes erronées.
![image](https://github.com/aminelfaquiri/fraud-Detection-in-Financial-Transactions/assets/81482544/8505e42c-fe97-4d28-ba41-6ddeb5e62402)

## Développement des API

### API des Données de Transaction

Dans le script `trans_api.py`, un point d'accès `/api/transactions` a été établi pour accéder aux données de transactions. Celles-ci incluent l'ID de transaction, la date et l'heure, le montant, la devise, les détails du commerçant, l'ID du client et le type de transaction.
<img width="828" alt="image" src="https://github.com/aminelfaquiri/fraud-Detection-in-Financial-Transactions/assets/81482544/e671d396-a555-4435-964e-8c6f27ef1ab8">

### API des Données Client

Un deuxième point d'accès, `/api/customers`, a été développé dans `trans_api.py` pour faciliter l'accès aux données clients, comprenant l'ID client, l'historique des comptes, les données démographiques et les modèles comportementaux.
<img width="923" alt="image" src="https://github.com/aminelfaquiri/fraud-Detection-in-Financial-Transactions/assets/81482544/56bc5b55-93b1-4605-984a-15431aa2736d">


### API des Données Externes

Une troisième API, `/api/externalData`, est également incluse dans `trans_api.py` pour récupérer des données externes, telles que les informations de liste noire, les scores de crédit et les rapports de fraude.
<img width="926" alt="image" src="https://github.com/aminelfaquiri/fraud-Detection-in-Financial-Transactions/assets/81482544/fa34ec26-d336-49a2-9cd0-21f4058e1bd9">


## Collecte et Intégration des Données

En utilisant les API développées dans le script `trans_api.py`, nous collectons les données transactionnelles, les données clients et les informations externes. Il est essentiel de garantir que les données collectées soient propres, pertinentes et dans un format adapté à l'analyse.

## Stockage et Gestion des Données avec Hive

Le projet englobe la conception et la mise en œuvre de tables Hive dans le script `trans_api.py` dédiées au stockage des données de transaction, des données clients et des informations externes. Des stratégies de partitionnement ou de bucketing sont appliquées pour une gestion efficace des données.

## Scripts pour Collecte et Insertion des Données

### Script : `get_api_data.py`

Le script `get_api_data.py` a été développé pour collecter les données depuis les différentes API, à savoir les données de transaction, les données clients et les informations externes. Ce script assure la récupération de données propres et pertinentes, prêtes à être intégrées dans notre système de stockage.

### Script : `insert_into_transaction.py`

Ce script insère les données de transaction collectées dans la table Hive dédiée, en utilisant les spécifications de conception établies précédemment. Les champs incluent l'ID de transaction, la date et l'heure, le montant, la devise, les détails du commerçant, l'ID du client, et le type de transaction.

### Script : `insert_into_customers.py`

Ce script est conçu pour insérer les données clients dans la table Hive correspondante. Les informations incluses couvrent l'ID client, l'historique des comptes, les données démographiques et les modèles comportementaux.

### Script : `insert_external_data.py`

Pour les données externes provenant de l'API, le script `insert_external_data.py` a été développé. Il assure l'insertion de ces informations dans la table Hive dédiée, couvrant des éléments tels que les informations de liste noire, les scores de crédit, et les rapports de fraude.

### Script : `insert_into_blacklist.py`

Enfin, le script `insert_into_blacklist.py` est spécifiquement conçu pour l'insertion de données dans la table Hive dédiée à la liste noire.

Ces scripts garantissent que les données collectées sont intégrées de manière organisée et efficace dans les tables Hive correspondantes, fournissant ainsi une base solide pour le développement ultérieur du système de détection de fraude basé sur les règles.

## Développement du Système de Détection de Fraude

Le développement du système de détection de fraude repose sur une approche stratégique visant à identifier et signaler les transactions potentiellement frauduleuses dans le cadre des opérations financières de "FinTech Innovations". Ce processus s'appuie sur une combinaison d'analyse de données transactionnelles, de critères de comportement client, et d'informations externes pour assurer une détection proactive des activités suspectes.

### Stratégie de Détection

La stratégie de détection de fraude est basée sur plusieurs critères et indicateurs, chacun conçu pour cibler des aspects spécifiques des transactions pouvant signaler un comportement frauduleux. Les principaux points de focalisation incluent :

1. **Recherche dans la Liste Noire**
   Le système compare les détails des commerçants impliqués dans les transactions avec une liste noire préétablie. Si une correspondance est identifiée, la transaction est signalée comme potentiellement frauduleuse.

2. **Détection des Lieux Inhabituels**
   Les transactions provenant de lieux considérés comme inhabituels sont scrutées de près. Cette approche vise à identifier des schémas de comportement atypiques pouvant indiquer une fraude potentielle.

3. **Montants Anormalement Élevés**
   Les transactions impliquant des montants significativement supérieurs à la moyenne sont considérées avec une attention particulière. Cela permet de repérer des transactions hors norme qui pourraient être liées à des activités frauduleuses.

4. **Fréquence Élevée de Transactions**
   L'analyse de la fréquence des transactions sur une période donnée est utilisée pour détecter des schémas inhabituels d'activité. Les seuils de fréquence sont établis pour identifier des comportements anormaux.

### Implémentation Technique

La mise en œuvre technique du système de détection de fraude repose sur l'utilisation de requêtes HiveQL dans le langage de requête Hive pour interroger les données stockées dans les tables Hive dédiées. Ces requêtes sont exécutées via un script Python, permettant une intégration fluide avec les données transactionnelles, les données clients, et les informations externes collectées par le biais des APIs.

### Résultats et Suivi

Les résultats de la détection de fraude sont affichés en temps réel et, le cas échéant, enregistrés dans un fichier CSV pour une analyse ultérieure. Ce suivi permet une évaluation continue de l'efficacité du système et la possibilité d'ajuster les critères de détection en fonction des nouvelles tendances de fraude identifiées.
<img width="733" alt="image" src="https://github.com/aminelfaquiri/fraud-Detection-in-Financial-Transactions/assets/81482544/561058d2-b156-43fd-bd44-91bc4381c730">

## DAG Apache Airflow pour l'Exécution Automatisée

### Aperçu du DAG

Afin de rationaliser et automatiser le processus de détection de fraude, un DAG Apache Airflow nommé `execute_scripts_dag` a été implémenté. Ce DAG orchestre l'exécution séquentielle de scripts Python critiques à des intervalles réguliers, assurant une détection de fraude opportune et efficace.

### Résumé des Tâches

1. **Tâche de Création de Connexion**
   - Établit les connexions nécessaires pour la récupération des données.

2. **Tâche d'Insertion des Transactions**
   - Insère les données de transaction dans le système pour analyse.

3. **Tâche d'Insertion des Clients**
   - Intègre les données clients dans le système de détection de fraude.

4. **Tâche d'Insertion des Données Externes**
   - Collecte et intègre des données externes pour une analyse approfondie.

5. **Tâche d'Insertion dans la Liste Noire**
   - Incorpore les données d'une liste noire pour identifier les entités suspectes.

6. **Tâche de Détection de Fraude**
   - Exécute des algorithmes de détection de fraude sur les données intégrées.

### Dépendances des Tâches

- Les dépendances des tâches assurent un flux d'exécution logique, en commençant par les tâches de préparation des données avant de passer à la phase réelle de détection de fraude.

### Planification

Le DAG est planifié pour s'exécuter à intervalles réguliers (toutes les 5 minutes), garantissant une exécution cohérente et opportune du pipeline de détection de fraude.

### Objectif

Ce DAG automatisé améliore l'efficacité du système de détection de fraude en automatisant la récupération, l'intégration et l'analyse des données. Il assure une approche proactive pour identifier les activités potentiellement frauduleuses dans les transactions financières.
<img width="612" alt="image (1)" src="https://github.com/aminelfaquiri/fraud-Detection-in-Financial-Transactions/assets/81482544/408223bd-db59-4b39-afac-563cfb60f4b7">

## Conclusion :
le projet de détection de fraude dans les transactions financières pour "FinTech Innovations" représente une approche holistique allant de la collecte de données à la détection en temps réel, intégrant des API robustes, une gestion efficace des données avec Hive, et un système de détection basé sur des règles avancées. L'introduction d'Apache Airflow, à travers le DAG execute_scripts_dag, automatise le flux de travail, assurant une exécution régulière. L'ensemble du projet vise à minimiser les risques de fraudes, à renforcer la confiance des clients, et à offrir une solution adaptative dans le paysage financier en constante évolution.
