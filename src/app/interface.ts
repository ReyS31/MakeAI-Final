export interface Coordinate {
    longitude:        number;
    latitude:         number;
    accidentSeverity: number;
    time:             string;
}

export interface Prediction{
    predictio: string;
}

export interface AccidentTotal{
    1: number;
    2: number;
    3: number;
}