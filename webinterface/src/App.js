import React, { useState } from "react";
import styled from "styled-components";

// Watch the Button tutorial
// http://react.school/ui/button

// Free React training
// http://react.school/join

// Free Material-UI template
// http://react.school/material-ui/templates

const theme = {
  blue: {
    default: "#3f51b5",
    hover: "#283593"
  },
  pink: {
    default: "#D0312D",
    hover: "#ad1457"
  }
};



const Button = styled.button`
  background-color: ${(props) => theme[props.theme].default};
  color: white;
  padding: 5px 15px;
  border-radius: 5px;
  outline: 0;
  text-transform: uppercase;
  display: flex;
   flexDirection: 'row',
   alignItems: 'center' //This will center you button
  margin: 10px 0px;
  cursor: pointer;
  box-shadow: 0px 2px 2px lightgray;
  transition: ease background-color 250ms;
  &:hover {
    background-color: ${(props) => theme[props.theme].hover};
  }
  &:disabled {
    cursor: default;
    opacity: 0.7;
  }
`;
Button.defaultProps = {
  theme: "blue"
};

function clickMe() {
  alert("Do Python Stuff");
}

const ButtonToggle = styled(Button)`
  opacity: 0.7;
  ${({ active }) =>
    active &&
    `
    opacity: 1; 
  `}
`;

const Tab = styled.button`
  padding: 10px 30px;
  cursor: pointer;
  opacity: 0.6;
  background: white;
  flexDirection: 'row';
  justifyContent: 'space-between'
  border: 0;
  outline: 0;
  border-bottom: 2px solid transparent;
  transition: ease border-bottom 250ms;
  ${({ active }) =>
    active &&
    `
    border-bottom: 2px solid black;
    opacity: 1;
  `}
`;

export default function App() {
  return (
    <>
	<h1>
	CS6903 Project
	</h1>
	
	<body>
	Here is where the questions regarding to what cryptographic primitve you want will be asked.
	</body>
	
	<p>
	INSERT QUESTION HERE
	</p>
	
	<div class="btnDiv">
		  <div>
			<Button onClick={clickMe}>Yes</Button>
		  </div>
		  <div>
			<Button theme="pink" onClick={clickMe}>
			  No
			</Button>
		</div>
	  </div>
    </>
  );
}
