package Data;

import java.io.*;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.HttpURLConnection;

import org.json.JSONArray;
import org.json.JSONObject;

public class ApiCallFileWriter{
    //function that reads the json data from an API, returns it as a String
    public static String read(URL url) {
        BufferedReader reader;
        String line;
        Exception ex;
        try{
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();

            //Request setup
            connection.setRequestMethod("GET");
            connection.setConnectTimeout(5000);
            connection.setReadTimeout(5000);
            int status = connection.getResponseCode();
            boolean read = false;
            System.out.println("Respone code:" + status);

            // print the content
            StringBuilder responseContent = new StringBuilder();
            if (status > 299){
                reader = new BufferedReader(new InputStreamReader(connection.getErrorStream()));
                while((line = reader.readLine()) != null){
                    responseContent.append(line);
                }
                reader.close();
            }
            else{
                reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
                while((line = reader.readLine())!=null){
                    responseContent.append(line);
                }
                read = true;
                reader.close();
            }
            if (read){
                return responseContent.toString();
            }
            else{
                return String.valueOf(status);
            }
        } catch(IOException e){
            e.printStackTrace();
            ex = e;
        }
        return ex.getMessage();
    }

    // function for writing the json data to a .json file
    public static void saveToFile(String data, String filename){
        JSONArray jsonArray = new JSONArray(data);
        try{
            BufferedWriter bw = new BufferedWriter(new FileWriter(filename));
            bw.write(jsonArray.toString());
            bw.close();
            System.out.println("The dataset has been written into a .json file.");
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }

    //Executing the read and saveToFile functions with appropriate variables
    public static void main(String[] args) throws MalformedURLException {
        URL url = new URL("https://data.nasa.gov/resource/gh4g-9sfh.json");
        String data = read(url);
        String filename = "meteorite_data.json";

        saveToFile(data, filename);
    }
}