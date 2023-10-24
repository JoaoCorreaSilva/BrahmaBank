import {StyleSheet} from 'react-native'

const styles = StyleSheet.create({
    container:{
        backgroundColor:'#D6D6B1',
        alignItems:'center',
        justifyContent:'center',
        flex:1,
    },
    caixa:{
        width:'80%',
        borderWidth:1,
        borderRadius: 5,
        padding:8,
        fontSize:25,
        marginTop:10,
    },
    title:{
        fontSize: 40,
        fontWeight:'bold'
    },
    caixas:{
        marginTop:100,
        alignItems:'center',
        justifyContent:'center',
        padding:40,
    },
    btnOk:{
        marginTop:20,
        borderWidth:1,
        borderRadius:10,
        width:'50%',
        height:50,
        backgroundColor:'#5a7bb0',
        alignItems:'center',
        justifyContent:'center',
    },
    box_login:{
        height: 80,
        marginTop: 10,
        padding: 20,

    },
})

export default styles