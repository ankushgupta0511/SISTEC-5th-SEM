import React, { useState } from 'react';
import { useModelPredictorMutation } from '../services/userAuthApi';
import { Grid, Alert, Typography, TextField, Box, Button } from "@mui/material";

// for pop window import library
import { Modal, ModalHeader } from "reactstrap"


// symtoms list of dict.
const symptoms_dict = { 'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111, 'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131 }




const DiseasePrediction = () => {

    const [poppopWindow, setPoppopWindow] = useState(false)


    const [modelPredictor, { isLoading }] = useModelPredictorMutation();
    const [server_error, setServerError] = useState({})
    const [server_msg, setServerMsg] = useState({})
    const [selectedSymptoms, setSelectedSymptoms] = useState([]);



    // Extract the keys (symptoms) from the dictionary
    const symptoms = Object.keys(symptoms_dict);   //  it convert into keys of dictionary
    // console.log('symptoms :- ',symptoms);
    // console.log('symptoms :- ',symptoms_dict);




    // Handler to manage checkbox selection
    const handleSelect = (event) => {
        const symptom = event.target.value;  // it give value which is selected
        const isChecked = event.target.checked;  // if value is checked then assign true ootherwise false.

        if (isChecked) {
            setSelectedSymptoms([...selectedSymptoms, symptom]);
        } else {
            setSelectedSymptoms(selectedSymptoms.filter(item => item !== symptom));
        }
    };


    const predicted_msg = (e) => {
        console.log('predicted_msg  :-  ',e)

    }


    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = new FormData(e.currentTarget);
        const actualData = {
            symtoms_name: data.get('selecet_symtoms'),
        }
        console.log('selecet_symtoms :- ', actualData);

        const res = await modelPredictor(actualData)

        if (res.error) {
            console.log('hello --> res.error')
            console.log(res.error.data.errors.symtoms_name);
            setServerMsg({})
            setServerError(res.error.data.errors)

        }
        if (res.data) {
            console.log('hello --> res.data')
            console.log(res.data.Predictions);
            setServerError({})
            setServerMsg(res.data.Predictions)
            document.getElementById("model-prediction-form").reset();

        }



    }

    return (

        <>
            {/* Pop Pop window modal and Headermodal */}
            <Modal
                isOpen={poppopWindow}
                toggle={() => setPoppopWindow(!poppopWindow)}
            >

                <ModalHeader
                    isOpen={poppopWindow}
                    toggle={() => setPoppopWindow(!poppopWindow)}
                >
                    <div className="bg-white shadow-[0_4px_12px_-5px_rgba(0,0,0,0.4)] p-6 w-full max-w-sm rounded-lg font-[sans-serif] overflow-hidden mx-auto mt-2">
                        <h3 className="text-xl font-bold text-gray-800">Heading</h3>
                        <p className="mt-3 text-sm text-gray-500 leading-relaxed">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed auctor.</p>

                        {/* <div className="relative flex items-center px-1 bg-gray-50 border-2 focus-within:border-[#007bff] focus-within:bg-white rounded-lg mt-6">
                            <input type="email" placeholder="Enter email"
                                className="p-3 text-gray-800 w-full text-sm bg-transparent outline-none" />
                            <button type="button"
                                className="px-5 py-2.5 rounded-lg text-white text-sm tracking-wider border-none outline-none bg-blue-600 hover:bg-blue-700">Send</button>
                        </div> */}
                    </div>

                </ModalHeader>

            </Modal>



            <Grid container justifyContent='center'>
                <Grid item sm={10} className="py-2">
                    <h1 className="text-2xl py-1" >Disease Predictions Page</h1>
                    <hr />

                    <h3 className="text-lg mb-1" >Select Symptoms:</h3>
                    {symptoms.map((symptom, index) => (
                        <label key={index}>
                            <input
                                type="checkbox"
                                value={symptom}
                                checked={selectedSymptoms.includes(symptom)}
                                onChange={handleSelect}
                            />
                            {symptom.replace(/_/g, ' ')} {/* Replace underscores with spaces for readability */}
                        </label>
                    ))}

                    <h4 className="text-lg mt-2">Selected Symptoms:</h4>

                    <form onSubmit={handleSubmit} id='model-prediction-form' >
                        <TextField margin='normal' required fullWidth name='selecet_symtoms' value={selectedSymptoms.map(symptom => symptom).join(', ')} label='Select Symtoms Address' />
                        {server_msg.msg ? <Alert security='success'>{server_msg.msg}</Alert> : ""}

                        {/* <input
                            type="text"
                            className='w-full mx-6 '
                            name='selecet_symtoms'
                            // value={selectedSymptoms.map(symptom => symptom.replace(/_/g, ' ')).join(', ')}
                            value={selectedSymptoms.map(symptom => symptom).join(', ')}
                            readOnly
                        /> */}
                        {server_error.symtoms_name ? <Typography style={{ fontSize: 12, color: 'red', paddingLeft: 10, }} > {server_error.symtoms_name[0]} </Typography> : ""}
                        <Box textAlign='center'>
                            <Button type='submit' variant='contained' sx={{ mt: 3, mb: 2, px: 5 }}>Predict Model</Button>
                        </Box>


                        <Box className='flex  justify-between'>
                            <Button onClick={() => { setPoppopWindow(true); predicted_msg(server_msg.predicted_disease); }} className='bg-red-200' sx={{ mt: 3, mb: 2, px: 5 }}>Diease</Button>
                            <Button onClick={() => { setPoppopWindow(true); predicted_msg(server_msg.predicted_precations); }} className='bg-red-200' sx={{ mt: 3, mb: 2, px: 5 }}>Precations</Button>
                            <Button onClick={() => { setPoppopWindow(true); predicted_msg(server_msg.predicted_descriptions); }} className='bg-red-200' sx={{ mt: 3, mb: 2, px: 5 }}>Description</Button>
                            <Button onClick={() => { setPoppopWindow(true); predicted_msg(server_msg.predicted_workout); }} className='bg-red-200' sx={{ mt: 3, mb: 2, px: 5 }}>Workout</Button>
                            <Button onClick={() => { setPoppopWindow(true); predicted_msg(server_msg.predicted_diets); }} className='bg-red-200' sx={{ mt: 3, mb: 2, px: 5 }}>Suggested Diets</Button>
                        </Box>
                    </form>


                    {/* <p>Home Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio earum officiis debitis vel tenetur quos animi vero voluptates reiciendis, omnis sed in libero temporibus deleniti pariatur expedita corporis officia. Odit enim, quasi facere magnam earum officiis ipsa aliquid impedit velit quibusdam dolor ex esse ratione explicabo quod, culpa temporibus? Dolorem deleniti doloremque maxime quas deserunt. Ex aspernatur saepe illo eaque corrupti placeat, aperiam nulla adipisci itaque quos necessitatibus iure at minus non delectus ratione quod ad. Alias dolore perferendis est expedita iure! Nostrum laborum tempore amet commodi voluptas accusamus enim repudiandae, quia odio cumque, laboriosam architecto illo! Aliquid, fuga quis.</p> */}
                </Grid>
            </Grid>


        </>
    )
}

export default DiseasePrediction



