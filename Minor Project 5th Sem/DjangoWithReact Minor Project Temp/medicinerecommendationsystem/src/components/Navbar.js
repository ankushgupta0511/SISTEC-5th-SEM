import React from 'react'
import { NavLink } from 'react-router-dom'


const Navbar = () => {
  return (
    <div className="w-full">
      <nav className="bg-[#9c27b0]">
        {/* <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"> */}
        <div className="max-w-full px-4 mx-auto ">
          <div className="flex justify-between items-center h-16">
            <div className="flex-shrink-0 text-white text-2xl font-semibold">
              Recommendention System
            </div>
            <div className="flex space-x-4">
              <NavLink
                to="/"
                className={({ isActive }) =>
                  isActive
                    ? 'bg-purple-900 text-white px-3 py-2 rounded-md text-sm font-medium'
                    : 'text-white px-3 py-2 rounded-md text-sm font-medium'
                }
              >
                Home
              </NavLink>

              <NavLink
                to="/contact"
                className={({ isActive }) =>
                  isActive
                    ? 'bg-purple-900 text-white px-3 py-2 rounded-md text-sm font-medium'
                    : 'text-white px-3 py-2 rounded-md text-sm font-medium'
                }
              >
                Contact
              </NavLink>

              <NavLink
                to="/diesase-prediction"
                className={({ isActive }) =>
                  isActive
                    ? 'bg-purple-900 text-white px-3 py-2 rounded-md text-sm font-medium'
                    : 'text-white px-3 py-2 rounded-md text-sm font-medium'
                }
              >
                Predictors
              </NavLink>

              <NavLink
                to="/login"
                className={({ isActive }) =>
                  isActive
                    ? 'bg-purple-900 text-white px-3 py-2 rounded-md text-sm font-medium'
                    : 'text-white px-3 py-2 rounded-md text-sm font-medium'
                }
              >
                Login/Registration
              </NavLink>
            </div>
          </div>
        </div>
      </nav>
    </div>
  )
}

export default Navbar
