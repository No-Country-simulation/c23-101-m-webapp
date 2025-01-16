import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import Login from './components/Login.jsx'
import Register from './components/Register.jsx'
import Home from './components/Home.jsx'


createRoot(document.getElementById('root')).render(
  <StrictMode>
    
    <Home />
    <Login />
    <Register />

  </StrictMode>,
)
