# show error
```
lack of concentration
```


# Tailwind auto build component

```
https://readymadeui.com/tailwind-components/cards
```

## import { Grid, TextField, Button, Box, Alert, Typography } from "@mui/material";

# install below liberary for above features

```
npm install @emotion/react @emotion/styled
npm install @mui/material@5.x @emotion/react@11.x @emotion/styled@11.x


npm cache clean --force
rm -rf node_modules
npm install

```

# Use Pop pop window template in react

```
npm install reactstrap
npm install bootstrap


// import this in index.js
import 'bootstrap/dist/css/bootstrap.css';


```

# tailwind css apply

```
//  source link :-  https://tailwindcss.com/docs/guides/create-react-app


1)
npm install -D tailwindcss
npx tailwindcss init


2)
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}



3)
@tailwind base;
@tailwind components;
@tailwind utilities;


// import this in index.js file
4)
import './index.css'


5)
npm run start

```

# install reac-router dom

```
npm install react-router-dom
```

# install this

```
npm install @mui/material
```

<section className='container w-[85%] flex flex-col mx-auto justify-center items-center'>
                <div className='w-full mt-12 '>

                    <h3 className="mb-4 font-semibold  text-2xl ">Select Symtoms </h3>
                    <hr className='py-3' />
                    <div>
                        <ul className="items-center w-full text-sm font-medium  bg-white border border-gray-200 rounded-lg sm:flex ">
                            <form action="" onClick={handleSubmit}>
                                <Select id='' name=''>

                                    <option value='one' className="w-full border-b  border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                                        <div className="flex items-center ps-3">
                                            <input id="vue-checkbox-list" type="checkbox" value="" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                                            <label for="vue-checkbox-list" className="w-full py-3 ms-2 text-sm font-medium  text-zinc-800">Vue JS</label>
                                        </div>
                                    </option>
                                    <option value='two' className="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                                        <div className="flex items-center ps-3">
                                            <input id="react1-checkbox-list" type="checkbox" value="" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                                            <label for="react1-checkbox-list" className="w-full py-3 ms-2 text-sm font-medium  text-zinc-800">React</label>
                                        </div>
                                    </option>
                                    <option className="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                                        <div className="flex items-center ps-3">
                                            <input id="react2-checkbox-list" type="checkbox" value="" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                                            <label for="react2-checkbox-list" className="w-full py-3 ms-2 text-sm font-medium  text-zinc-800">React</label>
                                        </div>
                                    </option>
                                    <option className="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                                        <div className="flex items-center ps-3">
                                            <input id="react3-checkbox-list" type="checkbox" value="" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                                            <label for="react3-checkbox-list" className="w-full py-3 ms-2 text-sm font-medium  text-zinc-800">React</label>
                                        </div>
                                    </option>
                                    <option className="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                                        <div className="flex items-center ps-3">
                                            <input id="react4-checkbox-list" type="checkbox" value="" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                                            <label for="react4-checkbox-list" className="w-full py-3 ms-2 text-sm font-medium  text-zinc-800">React</label>
                                        </div>
                                    </option>
                                    <option className="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                                        <div className="flex items-center ps-3">
                                            <input id="react5-checkbox-list" type="checkbox" value="" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                                            <label for="react5-checkbox-list" className="w-full py-3 ms-2 text-sm font-medium  text-zinc-800">React</label>
                                        </div>
                                    </option>

                                    <option className="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                                        <div className="flex items-center ps-3">
                                            <input id="react6-checkbox-list" type="checkbox" value="" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                                            <label for="react6-checkbox-list" className="w-full py-3 ms-2 text-sm font-medium  text-zinc-800">React</label>
                                        </div>
                                    </option>
                                    <option className="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                                        <div className="flex items-center ps-3">
                                            <input id="angular-checkbox-list" type="checkbox" value="" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                                            <label for="angular-checkbox-list" className="w-full py-3 ms-2 text-sm font-medium  text-zinc-800">Angular</label>
                                        </div>
                                    </option>
                                    <option className="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                                        <div className="flex items-center ps-3">
                                            <input id="django-checkbox-list" type="checkbox" value="" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                                            <label for="django-checkbox-list" className="w-full py-3 ms-2 text-sm font-medium  text-zinc-800">Django</label>
                                        </div>
                                    </option>
                                    <option className="w-full dark:border-gray-600">
                                        <div className="flex items-center ps-3">
                                            <input id="laravel-checkbox-list" type="checkbox" value="" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                                            <label for="laravel-checkbox-list" className="w-full py-3 ms-2 text-sm font-medium  text-zinc-800">Laravel</label>
                                        </div>
                                    </option>
                                </Select>

                                <button type='submit'>Model Predict</button>

                            </form>
                        </ul>
                    </div>

                </div>

            </section>
