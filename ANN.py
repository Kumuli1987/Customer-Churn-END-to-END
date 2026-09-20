# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler, LabelEncoder
# from sklearn.preprocessing import OneHotEncoder
# import pickle
# # !pip install tensorflow
# import tensorflow as tf
# from tensorflow.keras.models import Sequential, load_model

# from tensorflow.keras.layers import Dense
# from tensorflow.keras.callbacks import EarlyStopping, TensorBoard
# import streamlit as st
# import datetime

# data = pd.read_csv("Churn_Modelling.csv")
# data.head()

# data = data.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

# label_encoder_gender = LabelEncoder()
# data["Gender"] = label_encoder_gender.fit_transform(data["Gender"])

# onhot_encoder = OneHotEncoder()
# onhot_encoder_geo = onhot_encoder.fit_transform(data[["Geography"]])

# feature_names = onhot_encoder.get_feature_names_out(["Geography"])
# print(feature_names)

# onhot_encoder_geo.toarray()

# onhot_encoder_geo_df = pd.DataFrame(
#     onhot_encoder_geo.toarray(),
#     columns=['Geography_France', 'Geography_Germany', 'Geography_Spain'])

# data = pd.concat([data.drop("Geography",axis=1),onhot_encoder_geo_df],axis=1)

# with open("label_encoder_gender.pkl", "wb") as file:
#     pickle.dump(label_encoder_gender,file)
    
# with open("onhot_encoder_geo.pkl", "wb") as file:
#     pickle.dump(onhot_encoder,file)
    
# X = data.drop("Exited", axis=1)
# y = data[["Exited"]]

# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# scaller = StandardScaler()
# X_train = scaller.fit_transform(X_train)
# X_test = scaller.transform(X_test)

# with open("scaller.pkl", "wb") as file:
#     pickle.dump(scaller,file)
    
# print(data)
# print(X_train.shape)

# model = Sequential(
    
#     [Dense(64,activation="relu", input_shape= (X_train.shape[1],)), # first hidden layer
#      Dense(32,activation = "relu"), #Second Layer
#      Dense(1, activation="sigmoid") # output layer
        
        
#     ]
# )

# model.summary()
# import tensorflow
# opt = tensorflow.keras.optimizers.Adam(learning_rate=0.01)
# # loss = tensorflow.keras.losses.BinaryCrossentropy
# loss = tensorflow.keras.losses.BinaryCrossentropy()
# #compile model

# model.compile(optimizer=opt, loss=loss,metrics=["accuracy"])

# # set up tensor board
# log_dir = "log/fit"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

# tensorflow_callsback = TensorBoard(log_dir=log_dir,histogram_freq=1)

# early_stopping_callbacks = EarlyStopping(monitor="val_loss", patience=10, restore_best_weights=True)

# history = model.fit(
    
#     X_train,y_train,validation_data = (X_test,y_test), epochs=100,callbacks=[tensorflow_callsback,early_stopping_callbacks]
    
# )

# # model.save("model.h5")
# model.save("model.keras")

# # %load_ext TensorBoard

# # %TensorBoard -- logdir logs/fit



# import tensorboard
# import tensorflow as tf

# # Launch TensorBoard from Python
# # Make sure your log_dir matches the one you used in callbacks
# # log_dir = "log/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
# log_dir = "log/fit" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

# # Start TensorBoard programmatically
# from tensorboard import program
# tb = program.TensorBoard()
# tb.configure(argv=[None, "--logdir", log_dir])
# url = tb.launch()
# print(f"TensorBoard running at {url}")

# ## To open the tensorboard paste below in below command terminal
# # tensorboard --logdir=log --port=6006
# # tensorboard --logdir=log/fit --port=6006



# model = load_model("model.keras")

# with open("label_encoder_gender.pkl", "rb") as file:
#     label_encoder_gender = pickle.load(file)
    
# with open("onhot_encoder_geo.pkl", "rb") as file:
#     onhot_encoder_geo = pickle.load(file)
    
# with open("scaller.pkl", "rb") as file:
#     scaller = pickle.load(file)
    
# # Example input data
# input_data = {
#     'CreditScore': 600,
#     'Geography': 'France',
#     'Gender': 'Male',
#     'Age': 40,
#     'Tenure': 3,
#     'Balance': 60000,
#     'NumOfProducts': 2,
#     'HasCrCard': 1,
#     'IsActiveMember': 1,
#     'EstimatedSalary': 50000
# }    


# geo_encoded = onhot_encoder_geo.transform([[input_data['Geography']]]).toarray()
# geo_encoded_df = pd.DataFrame(geo_encoded, columns=onhot_encoder_geo.get_feature_names_out(['Geography']))
# geo_encoded_df

# input_df=pd.DataFrame([input_data])
# input_df

# input_df["Gender"] = label_encoder_gender.transform(input_df["Gender"])

# input_df = pd.concat([input_df.drop("Geography", axis=1),geo_encoded_df], axis=1)

# input_scalled = scaller.transform(input_df)

# prediction = model.predict(input_scalled)
# print(prediction)
# prediction_prob = prediction[0][0]

# if prediction_prob > 0.5:
#     print('The customer is likely to churn.')
# else:
#     print('The customer is not likely to churn.')
    
# ## Streamlit APP

# st.title("Customer Churn Prediction")
    
#  #print((onhot_encoder_geo).categories_[0])
#  #label_encoder_gender.classes_
#  geography = st.selectbox("Geography",onhot_encoder_geo.categories_[0])
#  gender = st.selectbox("Gneder",label_encoder_gender.classes_)
#  age = st.slider("Age", 18,92)
#  balance = st.number_input("Balance")
#  credit_score = st.number_input("Credit Score")
#  estimated_salary = st.number_input("Estimated Salary")
#  tenure = st.slider("Tenure", 0,10)
#  num_of_products = st.slider("Number of Product",1,4)
#  has_cr_card = st.selectbox("Has Credit Card", [0, 1])
#  is_active_number = st.selectbox("is_active_number", [0,1])
 
# # Prepare the input data
# input_data = pd.DataFrame({
#     'CreditScore': [credit_score],
#     'Gender': [label_encoder_gender.transform([gender])[0]],
#     'Age': [age],
#     'Tenure': [tenure],
#     'Balance': [balance],
#     'NumOfProducts': [num_of_products],
#     'HasCrCard': [has_cr_card],
#     'IsActiveMember': [is_active_member],
#     'EstimatedSalary': [estimated_salary]
# })

# # One-hot encode 'Geography'
# geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()
# geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))

# # Combine one-hot encoded columns with input data
# input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

# # Scale the input data
# input_data_scaled = scaler.transform(input_data)


# # Predict churn
# prediction = model.predict(input_data_scaled)
# prediction_proba = prediction[0][0]

# st.write(f'Churn Probability: {prediction_proba:.2f}')

# if prediction_proba > 0.5:
#     st.write('The customer is likely to churn.')
# else:
#     st.write('The customer is not likely to churn.')
 
 
 
# ===========================================================================================================
 
import pandas as pd
import pickle
import datetime

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping, TensorBoard


# ==========================================
# 1. Load dataset
# ==========================================

data = pd.read_csv("Churn_Modelling.csv")

# Remove unnecessary columns
data = data.drop(
    ["RowNumber", "CustomerId", "Surname"],
    axis=1
)


# ==========================================
# 2. Encode Gender
# ==========================================

label_encoder_gender = LabelEncoder()

data["Gender"] = label_encoder_gender.fit_transform(
    data["Gender"]
)

# Save gender encoder
with open("label_encoder_gender.pkl", "wb") as file:
    pickle.dump(label_encoder_gender, file)


# ==========================================
# 3. Encode Geography
# ==========================================

onehot_encoder_geo = OneHotEncoder()

geo_encoded = onehot_encoder_geo.fit_transform(
    data[["Geography"]]
)

geo_encoded_df = pd.DataFrame(
    geo_encoded.toarray(),
    columns=onehot_encoder_geo.get_feature_names_out(
        ["Geography"]
    ),
    index=data.index
)

# Remove original Geography and add encoded columns
data = pd.concat(
    [
        data.drop("Geography", axis=1),
        geo_encoded_df
    ],
    axis=1
)

# Save geography encoder
with open("onehot_encoder_geo.pkl", "wb") as file:
    pickle.dump(onehot_encoder_geo, file)


# ==========================================
# 4. Separate input and output
# ==========================================

X = data.drop("Exited", axis=1)
y = data["Exited"]


# ==========================================
# 5. Train/Test split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# 6. Scale features
# ==========================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Save scaler
with open("scaler.pkl", "wb") as file:
    pickle.dump(scaler, file)


# ==========================================
# 7. Create neural network
# ==========================================

model = Sequential([
    tf.keras.Input(shape=(X_train.shape[1],)),

    Dense(
        64,
        activation="relu"
    ),

    Dense(
        32,
        activation="relu"
    ),

    Dense(
        1,
        activation="sigmoid"
    )
])


# ==========================================
# 8. Compile
# ==========================================

optimizer = tf.keras.optimizers.Adam(
    learning_rate=0.01
)

model.compile(
    optimizer=optimizer,
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.summary()


# ==========================================
# 9. TensorBoard
# ==========================================

log_dir = (
    "logs/fit/"
    + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
)

tensorboard_callback = TensorBoard(
    log_dir=log_dir,
    histogram_freq=1
)

early_stopping_callback = EarlyStopping(
    monitor="val_loss",
    patience=10,
    restore_best_weights=True
)


# ==========================================
# 10. Train
# ==========================================

history = model.fit(
    X_train,
    y_train,
    validation_data=(X_test, y_test),
    epochs=100,
    callbacks=[
        tensorboard_callback,
        early_stopping_callback
    ]
)


# ==========================================
# 11. Save trained model
# ==========================================

model.save("model.keras")

print("Model training completed.")
print("Saved model.keras")
print("Saved scaler.pkl")
print("Saved label_encoder_gender.pkl")
print("Saved onehot_encoder_geo.pkl")