import { Timbre } from './Interface';
import React from 'react';

interface FormProps {
    onAdd: (timbre: Timbre) => void;
  }
  
export const Form: React.FC<FormProps> = ({ onAdd }) => {

    const [message, setMessage] = React.useState('');
   
    const handleSubmit = (event: React.FormEvent) => {
      event.preventDefault();
      const newTimbre: Timbre = {
        datetime: 'null',  // reemplaza con el valor que necesites
        message: message,  // reemplaza con el valor que necesites
    }
    
      onAdd(newTimbre);
      setMessage('');
    };
  
    return (
      <form onSubmit={handleSubmit}>
        <input
          value={message}
          onChange={(event) => setMessage(event.target.value)}
          required
        />
        <button type="submit">Agregar</button>
      </form>
    );
  };
  