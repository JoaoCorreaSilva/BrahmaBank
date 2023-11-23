import React, { useState, useEffect } from 'react';
import { View, Text } from 'react-native';
import Icon from 'react-native-vector-icons/Feather';
import styles from './styles';

export default function Home({ navigation, route }) {
  const [cont, setCont] = useState(0);

  const Menu = () => {
    return (
      <View style={styles.cima}>
        <View>
          <Text>Descrição do cabeçalho</Text>
        </View>
        {/* O restante do conteúdo do seu componente */}
        <Text>Outro conteúdo do componente...</Text>
      </View>
    );
  };

  return (
    <View style={styles.container}>
      <Menu />
      <View>
        <Text style={styles.txt}></Text>
      </View>
      <View>
        <Text>Olá Paula</Text>
        <Icon name="user" size={40} color="black" />
      </View>
    </View>
  );
}
