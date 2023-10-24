import { initializeApp } from "firebase/app";
import { getFirestore } from 'firebase/firestore'
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";
import {getStorage} from 'firebase/storage'


const firebaseConfig = {
  apiKey: "AIzaSyBOqf1pIkx03-BuIQKehYWFpuabsTd_P0M",
  authDomain: "ds-mb-2-2023-lin.firebaseapp.com",
  projectId: "ds-mb-2-2023-lin",
  storageBucket: "ds-mb-2-2023-lin.appspot.com",
  messagingSenderId: "1072346549698",
  appId: "1:1072346549698:web:835ee116cc5db5d0a19a5b"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app)
const auth = getAuth(app);
const storage = getStorage(app)

export {auth, db, storage}