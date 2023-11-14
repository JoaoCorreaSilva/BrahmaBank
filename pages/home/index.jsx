import React, { useState, useEffect } from 'react';
import { View, Text } from 'react-native';
import Icon from 'react-native-vector-icons/Feather'; // Importe o ícone desejado
import styles from './styles';

export default function Home({ navigation, route }) {
  const [cont, setCont] = useState(0);

  return (
    <View style={styles.container}>
      <View>
        <Text style={styles.txt}></Text>
      </View>
      <View>
        <Text>Olá Paula</Text>
        <Icon name="user" size={40} color="black" /> {/* Exemplo de uso de um ícone */}
      </View>
    </View>
  );
}
