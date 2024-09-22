import './App.css';
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Contact from './pages/Contact';
import Home from './pages/Home';
import DiseasePrediction from './pages/DiseasePrediction';


function App() {
  return (
    <BrowserRouter>
      <Navbar />


      <Routes>

        {/* <Route path='/' index element={ <Navbar/> }/> */}

        <Route path='' element={ <Home />} />
        <Route path='contact' element={<Contact />} />
        <Route path='diesase-prediction' element={<DiseasePrediction />} />
        {/* <Route path='/' element={ <Footer/> }/> */}


      </Routes>

    </BrowserRouter>
  );
}

export default App;
