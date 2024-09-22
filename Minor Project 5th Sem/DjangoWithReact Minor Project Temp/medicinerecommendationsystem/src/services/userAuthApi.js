import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const userAuthApi = createApi({
    reducerPath: 'userAuthApi',
    baseQuery: fetchBaseQuery({ baseUrl: 'http://127.0.0.1:8000/api/user/' }),
    endpoints: (builder) => ({

        // below mutation use for data modify (like update delete etc.)
        modelPredictor: builder.mutation({
            query: (actualData) => {


                return {
                    url: `predict/`,
                    method: 'POST',
                    body: actualData,
                    headers: {
                        'Content-type': 'application/json',
                    }

                }
            }
        }),



    }),
})

export const { useModelPredictorMutation } = userAuthApi