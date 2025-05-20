// Import Firebase modules
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js";
import { getAuth, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.0.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/9.0.0/firebase-firestore.js";

// Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyD39N626JBDn5d5lk6mLHc82DNCF4aEAgc",
  authDomain: "project-c6b15.firebaseapp.com",
  projectId: "project-c6b15",
  storageBucket: "project-c6b15.firebasestorage.app",
  messagingSenderId: "370167031967",
  appId: "1:370167031967:web:1849f3c656aa3c557cdaaa",
  measurementId: "G-T12FQ6XYNZ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app); // if needed

// Login handler
document.getElementById('login-form').addEventListener('submit', function (event) {
  event.preventDefault(); // Stop form from submitting traditionally

  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  localStorage.setItem('profile', JSON.stringify({ email }));

  signInWithEmailAndPassword(auth, email, password)
    .then(userCredential => {
      console.log('User logged in:', userCredential.user);
      window.location.href = '/profile';
    })
    .catch(error => {
      console.error(error.code, error.message);
      alert('Login failed: ' + error.message);
    });
});
