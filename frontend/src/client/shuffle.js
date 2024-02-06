import axios from 'axios';

const shuffleData = async (input) => {
  const url = 'http://127.0.0.1:8000/shuffle/';
  const data = {input: input}

  try {
    const response = await axios.post(url, data);
    console.log('Shuffle response:', response.data.data);
    return await response.data.data
    // Handle the response as needed
  } catch (error) {
    console.error('Error during shuffle request:', error);
    // Handle the error as needed
  }
  return ['error']
};

export default shuffleData;
shuffleData([1,2,21,12]);


// Call the function to make the request
