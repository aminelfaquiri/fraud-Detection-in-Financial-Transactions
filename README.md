# Détection de Fraude dans les Transactions Financières
![image](https://github.com/aminelfaquiri/fraud-Detection-in-Financial-Transactions/assets/81482544/01e1cc28-e3cc-4836-a748-7e6061708159)

## Introduction

La société "FinTech Innovations" est actuellement confrontée à un défi croissant lié aux transactions frauduleuses, mettant en péril la confiance de nos clients et entraînant des pertes financières importantes. Pour relever ce défi, notre initiative vise à mettre en place un système de détection de fraude basé sur l'analyse de données transactionnelles, de données clients et d'informations externes. L'objectif principal est de détecter en temps réel les activités suspectes tout en minimisant les fausses alertes.

## Objectif du Projet

En tant que développeur Data, l'objectif global demeure la création d'une API nommée `trans_api.py` et la mise en œuvre d'un système de détection de fraude capable d'identifier rapidement les activités suspectes tout en réduisant au maximum les alertes erronées.

## Développement des API

### API des Données de Transaction

Dans le script `trans_api.py`, un point d'accès `/api/transactions` a été établi pour accéder aux données de transactions. Celles-ci incluent l'ID de transaction, la date et l'heure, le montant, la devise, les détails du commerçant, l'ID du client et le type de transaction.

### API des Données Client

Un deuxième point d'accès, `/api/customers`, a été développé dans `trans_api.py` pour faciliter l'accès aux données clients, comprenant l'ID client, l'historique des comptes, les données démographiques et les modèles comportementaux.

### API des Données Externes

Une troisième API, `/api/externalData`, est également incluse dans `trans_api.py` pour récupérer des données externes, telles que les informations de liste noire, les scores de crédit et les rapports de fraude.

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


