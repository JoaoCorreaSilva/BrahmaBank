import { StyleSheet } from "react-native"

const styles = StyleSheet.create({
    container:{
        backgroundColor: '#D6D6B1',
        alignItems: 'center', 
        justifyContent:'center', 
        width: '100%',
        flex:1,
        height: 20,
    },
    txt:{
        fontSize: 30,
        color:'#fff'
    },
    cima:{
        height:600,
        width:300,
    },
    viewBotoes:{
        display: "flex",
        flexDirection: "row",
        justifyContent: "space-around",
        width: "100%"
    }
})

export default styles