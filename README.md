# PetCare - Sistema de Controle de Animais de Estimação  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)  
![FastAPI](https://img.shields.io/badge/FastAPI-0.85-green)  
![MongoDB](https://img.shields.io/badge/MongoDB-5.0-yellowgreen)  
![Docker](https://img.shields.io/badge/Docker-3.8-lightblue)  

Um sistema completo para gerenciamento de animais de estimação, incluindo cadastro de usuários, pets, controle de vacinas e relatórios.  

## 📌 Funcionalidades  
✔ **Usuários**: Cadastro e autenticação segura 
✔ **Animais**: Cadastro de pets com espécie, raça e histórico médico  
✔ **Vacinas**: Registro de vacinas com alertas de revacinação  
✔ **Relatórios**: Exportação em PDF para veterinários  
✔ **Admin**: Painel para gerenciamento de raças e usuários  

## Diagrama UML
<a href="https://lucid.app/lucidchart/d1b30041-383d-41c0-8a13-b37fa799b342/edit?invitationId=inv_91fb7c69-8510-4c5b-843c-db9579347cc5&page=0_0" target="_blank">Diagrama UML adaptado para python</a>

## Historias de usuário
<a href="https://miro.com/app/board/uXjVK1MCAho=/" target="_blank">Hitorias de usuário</a>

## 🛠 Tecnologias  
| Área         | Tecnologias |  
|--------------|------------|  
| **Backend**  | Python, FastAPI, Pydantic |  
| **Database** | MongoDB (com PyMongo) |  
| **Frontend** | React |  
| **Infra**    | Docker, Docker Compose |  
| **Testes**   | Pytest |  

## 🚀 Como Executar  

### 1. Com Docker 
```bash  
git clone https://github.com/Ericcs10/ControleAnimalDeEstimacao.git  
cd ControleAnimalDeEstimacao  

# Inicia a API + MongoDB  
docker-compose up --build
