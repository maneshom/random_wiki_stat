import React , { Component } from "react";
import { render } from "react-dom";
import { Card, CardColumns,Container  } from 'react-bootstrap';
import {XYPlot, XAxis, YAxis, HorizontalGridLines, HorizontalBarSeries, VerticalBarSeries, VerticalGridLines} from 'react-vis';

class App extends Component {
    constructor(props){
        super(props);
        this.state = {
            data: [],
            loaded: false,
            placeholder: "Loading"
        };
    }
    componentDidMount()
    {
        fetch("api/wiki")
        .then(response => {
            if (response.status > 400){
                return this.setState(() => {
                    return { placeholder: "Something went wrong!"};
                });
            }
            return response.json();
        })
        .then(data => {
            this,this.setState(() => {
                return {
                    data,
                    loaded:true
                };
            });
        });
    }
    render() {
        return (

        <Container>
            <CardColumns>

                    {this.state.data.map(contact => {
                    return (
                        <Card key={contact.id}>
                        <Card.Title>
                        -- <a href={contact.link}>{contact.title}</a>
                        </Card.Title>
                        <Card.Body>
                          
                          <XYPlot key={contact.id} width={300} height={300} xType="ordinal">
                        <VerticalGridLines />
                        <VerticalBarSeries data={[{y: contact.no_of_image, x: "Images"}, {y: contact.no_of_link, x: "Links"}]} />
                        <XAxis />
                        <YAxis />
                      </XYPlot>
                        </Card.Body>
                        <Card.Footer>
                          <small className="text-muted">Added to DB: {contact.created_on}</small>
                        </Card.Footer>
                      </Card>

                    );
                })}

            </CardColumns>
        </Container>

        );
    }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);