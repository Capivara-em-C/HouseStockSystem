#!/bin/bash

FALHA_DE_COMPLEXIDADE=$(radon mi * -nb)

if [[ $FALHA_DE_COMPLEXIDADE ]]; then
	echo -e "\033[41m\n"
	echo -e "==========================================================================================="
	echo -e ">>> ERRO:"
	echo -e "-------------------------------------------------------------------------------------------"
	echo -e "	Complexidade do código ultrapaçou o limite configurado para o sistema!"
	echo -e "	Por favor diminua a complexidade do seu código ou solicite a alteração do limite."
	echo -e "-------------------------------------------------------------------------------------------"
	echo -e "\033[49m"
	radon cc * -nb
	echo -e "\033[41m"
	echo -e "==========================================================================================="
	echo -e "\033[49m"
	exit 1
else
	echo -e "\033[42m\n\nParabéns, seu código está com complexidade boa (*0*)!\n\033[49m"
fi
